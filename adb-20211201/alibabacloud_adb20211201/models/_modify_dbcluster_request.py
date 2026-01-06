# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBClusterRequest(DaraModel):
    def __init__(
        self,
        compute_resource: str = None,
        dbcluster_id: str = None,
        enable_default_resource_pool: bool = None,
        product_form: str = None,
        region_id: str = None,
        reserved_node_count: int = None,
        reserved_node_size: str = None,
        storage_resource: str = None,
    ):
        # The reserved computing resources. Valid values: 0ACU to 4096ACU. The value must be in increments of 16ACU. Each ACU is approximately equal to 1 core and 4 GB memory.
        # 
        # >  This parameter must be specified with a unit.
        self.compute_resource = compute_resource
        # The ID of the AnalyticDB for MySQL Data Lakehouse Edition cluster.
        # 
        # >  You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/454250.html) operation to query the IDs of all AnalyticDB for MySQL Data Lakehouse Edition clusters within a region.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Specifies whether to allocate all reserved computing resources to the user_default resource group. Valid values:
        # 
        # *   true (default)
        # *   false
        self.enable_default_resource_pool = enable_default_resource_pool
        self.product_form = product_form
        # The region ID of the cluster.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/454314.html) operation to query the most recent region list.
        self.region_id = region_id
        self.reserved_node_count = reserved_node_count
        self.reserved_node_size = reserved_node_size
        # The reserved storage resources. Valid values: 0ACU to 2064ACU. The value must be in increments of 24ACU. Each ACU is approximately equal to 1 core and 4 GB memory.
        # 
        # >  This parameter must be specified with a unit.
        self.storage_resource = storage_resource

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compute_resource is not None:
            result['ComputeResource'] = self.compute_resource

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.enable_default_resource_pool is not None:
            result['EnableDefaultResourcePool'] = self.enable_default_resource_pool

        if self.product_form is not None:
            result['ProductForm'] = self.product_form

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reserved_node_count is not None:
            result['ReservedNodeCount'] = self.reserved_node_count

        if self.reserved_node_size is not None:
            result['ReservedNodeSize'] = self.reserved_node_size

        if self.storage_resource is not None:
            result['StorageResource'] = self.storage_resource

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputeResource') is not None:
            self.compute_resource = m.get('ComputeResource')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EnableDefaultResourcePool') is not None:
            self.enable_default_resource_pool = m.get('EnableDefaultResourcePool')

        if m.get('ProductForm') is not None:
            self.product_form = m.get('ProductForm')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReservedNodeCount') is not None:
            self.reserved_node_count = m.get('ReservedNodeCount')

        if m.get('ReservedNodeSize') is not None:
            self.reserved_node_size = m.get('ReservedNodeSize')

        if m.get('StorageResource') is not None:
            self.storage_resource = m.get('StorageResource')

        return self

