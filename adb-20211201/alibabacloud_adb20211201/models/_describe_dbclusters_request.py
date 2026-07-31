# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClustersRequest(DaraModel):
    def __init__(
        self,
        dbcluster_description: str = None,
        dbcluster_ids: str = None,
        dbcluster_status: str = None,
        dbcluster_version: str = None,
        page_number: int = None,
        page_size: int = None,
        product_version: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tag: List[main_models.DescribeDBClustersRequestTag] = None,
    ):
        # The cluster description.
        # 
        # - Cannot start with `http://` or `https://`.
        # 
        # - The description must be 2 to 256 characters long.
        self.dbcluster_description = dbcluster_description
        # The cluster ID.
        # 
        # If you omit this parameter, the operation returns information about all clusters in the specified region.
        self.dbcluster_ids = dbcluster_ids
        # The cluster status. Valid values:
        # 
        # - **Preparing**: The cluster is preparing.
        # 
        # - **Creating**: The cluster is being created.
        # 
        # - **Running**: The cluster is running.
        # 
        # - **Deleting**: The cluster is being deleted.
        # 
        # - **Restoring**: The cluster is being restored from a backup.
        # 
        # - **ClassChanging**: The cluster specifications are changing.
        # 
        # - **NetAddressCreating**: A network connection is being created for the cluster.
        # 
        # - **NetAddressDeleting**: The network connection of the cluster is being deleted.
        # 
        # - **NetAddressModifying**: The network connection of the cluster is being modified.
        self.dbcluster_status = dbcluster_status
        # The cluster version. Valid values:
        # 
        # - **3.0**: Data Warehouse edition.
        # 
        # - **5.0** (default): Includes the Lakehouse, Enterprise, and Basic editions.
        # 
        # - **All**: All editions, including the Data Warehouse, Lakehouse, Enterprise, and Basic editions.
        self.dbcluster_version = dbcluster_version
        # The page number. The value must be a positive integer. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values:
        # 
        # - **30** (default)
        # 
        # - **50**
        # 
        # - **100**
        self.page_size = page_size
        # The product version. Valid values:
        # 
        # - **EnterpriseVersion**: Enterprise edition.
        # 
        # - **BasicVersion**: Basic edition.
        # 
        # > If you omit this parameter, the operation returns clusters of all product versions.
        self.product_version = product_version
        # The region ID.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/454314.html) operation to query the IDs of available regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group. If you omit this parameter, the operation returns information about clusters in all resource groups.
        self.resource_group_id = resource_group_id
        # The tags to filter clusters by.
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
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description

        if self.dbcluster_ids is not None:
            result['DBClusterIds'] = self.dbcluster_ids

        if self.dbcluster_status is not None:
            result['DBClusterStatus'] = self.dbcluster_status

        if self.dbcluster_version is not None:
            result['DBClusterVersion'] = self.dbcluster_version

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_version is not None:
            result['ProductVersion'] = self.product_version

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')

        if m.get('DBClusterIds') is not None:
            self.dbcluster_ids = m.get('DBClusterIds')

        if m.get('DBClusterStatus') is not None:
            self.dbcluster_status = m.get('DBClusterStatus')

        if m.get('DBClusterVersion') is not None:
            self.dbcluster_version = m.get('DBClusterVersion')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductVersion') is not None:
            self.product_version = m.get('ProductVersion')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

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
        # The tag key.
        self.key = key
        # The tag value.
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

