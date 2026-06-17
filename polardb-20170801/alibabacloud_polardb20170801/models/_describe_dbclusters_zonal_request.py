# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClustersZonalRequest(DaraModel):
    def __init__(
        self,
        cloud_provider: str = None,
        connection_string: str = None,
        dbcluster_description: str = None,
        dbcluster_ids: str = None,
        dbcluster_status: str = None,
        dbnode_ids: str = None,
        dbtype: str = None,
        dbversion: str = None,
        describe_type: str = None,
        expired: str = None,
        max_results: int = None,
        next_token: str = None,
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
        tag: List[main_models.DescribeDBClustersZonalRequestTag] = None,
    ):
        # The cloud service provider.
        self.cloud_provider = cloud_provider
        # The database endpoint.
        self.connection_string = connection_string
        # The description of the cluster. Fuzzy search is supported.
        self.dbcluster_description = dbcluster_description
        # The cluster ID. To specify multiple cluster IDs, separate them with commas (,).
        self.dbcluster_ids = dbcluster_ids
        # The status of the cluster.
        self.dbcluster_status = dbcluster_status
        # The node ID. You can specify multiple node IDs. Separate them with commas (,).
        self.dbnode_ids = dbnode_ids
        # The database type. Valid values:
        # 
        # - MySQL
        # 
        # - PostgreSQL
        # 
        # - Oracle
        self.dbtype = dbtype
        # The database version.
        self.dbversion = dbversion
        # The query mode. Set the value to \\`Simple\\`. In this mode, only the basic metadata of the clusters is returned.
        self.describe_type = describe_type
        # Specifies whether the cluster has expired. Valid values:
        # 
        # - true
        # 
        # - false
        self.expired = expired
        # The maximum number of entries to return for the current request. Default value: 10.
        self.max_results = max_results
        # A token used to retrieve the next page of results. Set this parameter to the \\`NextToken\\` value returned from the previous API call. You do not need to specify this parameter for the first call.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. The value must be an integer that is greater than 0 and does not exceed the maximum value of the Integer data type. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values: 30, 50, and 100.
        # 
        # Default value: 30.
        self.page_size = page_size
        # The billing method. Valid values:
        # 
        # - Postpaid: pay-as-you-go
        # 
        # - Prepaid: subscription
        self.pay_type = pay_type
        # Filters for clusters created in the last N days. Valid values: 0 to 15.
        self.recent_creation_interval = recent_creation_interval
        # Filters for clusters that expire in N days. Valid values: 0 to 15.
        self.recent_expiration_interval = recent_expiration_interval
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The list of tags.
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
        if self.cloud_provider is not None:
            result['CloudProvider'] = self.cloud_provider

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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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
        if m.get('CloudProvider') is not None:
            self.cloud_provider = m.get('CloudProvider')

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

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

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
                temp_model = main_models.DescribeDBClustersZonalRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeDBClustersZonalRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag \\`n\\`. You can filter clusters by specifying up to 20 tags. The \\`n\\` must be a unique and consecutive integer that starts from 1. \\`Tag.n.Key\\` corresponds to \\`Tag.n.Value\\`.
        self.key = key
        # The value of the tag key.
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

