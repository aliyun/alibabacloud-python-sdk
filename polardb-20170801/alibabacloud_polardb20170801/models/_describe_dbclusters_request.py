# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClustersRequest(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        dbcluster_description: str = None,
        dbcluster_ids: str = None,
        dbcluster_status: str = None,
        dbnode_ids: str = None,
        dbtype: str = None,
        dbversion: str = None,
        describe_type: str = None,
        expired: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        pay_type: str = None,
        recent_creation_interval: int = None,
        recent_expiration_interval: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.DescribeDBClustersRequestTag] = None,
    ):
        # The endpoint of the cluster.
        self.connection_string = connection_string
        # The description of the cluster. Fuzzy match is supported.
        self.dbcluster_description = dbcluster_description
        # The ID of the cluster. Separate multiple cluster IDs with commas (,).
        self.dbcluster_ids = dbcluster_ids
        # The state of the cluster that you want to query. For information about valid values, see [Cluster states](https://help.aliyun.com/document_detail/99286.html).
        self.dbcluster_status = dbcluster_status
        # The ID of the node. You can specify multiple node IDs. Separate multiple node IDs with commas (,).
        self.dbnode_ids = dbnode_ids
        # The database engine that the cluster runs. Valid values:
        # 
        # *   **MySQL**
        # *   **PostgreSQL**
        # *   **Oracle**
        self.dbtype = dbtype
        # The database engine version of the cluster.
        self.dbversion = dbversion
        # The query mode of the list. The value Simple indicates that the simple mode is used. In this mode, only the basic metadata information of the cluster is returned.
        # 
        # > If you do not specify this parameter, the detailed mode is used by default. Detailed information about the cluster is returned.
        self.describe_type = describe_type
        # Specifies whether the cluster has expired. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.expired = expired
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. The value must be a positive integer that does not exceed the maximum value of the INTEGER data type. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values: **30**, **50**, and **100**.
        # 
        # Default value: **30**.
        self.page_size = page_size
        # The billing method. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go
        # *   **Prepaid**: subscription
        self.pay_type = pay_type
        # Filters clusters created in the last N days. Valid values: 0 to 15.
        self.recent_creation_interval = recent_creation_interval
        # Filters clusters that expire after N days. Valid values: 0 to 15.
        self.recent_expiration_interval = recent_expiration_interval
        # The region ID of the cluster.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query the available regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags of the cluster.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description

        if self.dbcluster_ids is not None:
            result['DBClusterIds'] = self.dbcluster_ids

        if self.dbcluster_status is not None:
            result['DBClusterStatus'] = self.dbcluster_status

        if self.dbnode_ids is not None:
            result['DBNodeIds'] = self.dbnode_ids

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.describe_type is not None:
            result['DescribeType'] = self.describe_type

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.recent_creation_interval is not None:
            result['RecentCreationInterval'] = self.recent_creation_interval

        if self.recent_expiration_interval is not None:
            result['RecentExpirationInterval'] = self.recent_expiration_interval

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')

        if m.get('DBClusterIds') is not None:
            self.dbcluster_ids = m.get('DBClusterIds')

        if m.get('DBClusterStatus') is not None:
            self.dbcluster_status = m.get('DBClusterStatus')

        if m.get('DBNodeIds') is not None:
            self.dbnode_ids = m.get('DBNodeIds')

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('DescribeType') is not None:
            self.describe_type = m.get('DescribeType')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('RecentCreationInterval') is not None:
            self.recent_creation_interval = m.get('RecentCreationInterval')

        if m.get('RecentExpirationInterval') is not None:
            self.recent_expiration_interval = m.get('RecentExpirationInterval')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeDBClustersRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeDBClustersRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag. You can use tags to filter clusters. You can specify up to 20 tags. N specifies the serial number of each tag. The values that you specify for N must be unique and consecutive integers that start from 1. The value of Tag.N.Key is Tag.N.Value.
        # 
        # > The tag key can be up to 64 characters in length and cannot start with `aliyun`, `acs:`, `http://`, or `https://`.
        self.key = key
        # The value of the tag.
        # 
        # > The tag value can be up to 64 characters in length and cannot start with `aliyun`, `acs:`, `http://`, or `https://`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

