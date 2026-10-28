# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBClusterRequest(DaraModel):
    def __init__(
        self,
        ainode_number: int = None,
        ainode_spec: str = None,
        compute_resource: str = None,
        dbcluster_id: str = None,
        enable_default_resource_pool: bool = None,
        product_form: str = None,
        product_version: str = None,
        region_id: str = None,
        reserved_node_count: int = None,
        reserved_node_size: str = None,
        storage_resource: str = None,
    ):
        # The number of AI nodes.
        self.ainode_number = ainode_number
        # The AI node specifications.
        self.ainode_spec = ainode_spec
        # The reserved compute resources. Valid values: 0 ACU to 4096 ACU. Step: 16. 1 ACU is approximately equal to 1 core and 4 GB of memory.
        # > Include the unit when you specify this parameter.
        self.compute_resource = compute_resource
        # The ID of the Data Lakehouse Edition cluster.
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/454250.html) operation to query the ID of the Data Lakehouse Edition cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Specifies whether to allocate all reserved compute resources to the default resource group (user_default). Valid values:
        # - true (default): Yes.
        # - false: No.
        self.enable_default_resource_pool = enable_default_resource_pool
        # The product form. Valid values:
        # - **IntegrationForm**: Integration form.
        # - **LegacyForm**: Data Lakehouse Edition.
        self.product_form = product_form
        # The target product version. When you switch from LegacyForm to IntegrationForm Enterprise Edition in-place, set this parameter to enterprise_version and specify ProductForm, ReservedNodeSize, and ReservedNodeCount at the same time.
        self.product_version = product_version
        # The region ID.
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/454314.html) operation to query the region ID of the specified Data Lakehouse Edition cluster.
        self.region_id = region_id
        # The number of reserved nodes. 
        # - For Enterprise Edition, the default value is 3 and the step is 3.
        # - For Basic Edition, the default value is 1.
        # > Specify this parameter only when ProductForm is set to IntegrationForm.
        self.reserved_node_count = reserved_node_count
        # The node specifications for reserved storage resources. Valid values: 8 ACU, 12 ACU, and 16 ACU.
        # > Include the unit when you specify this parameter. Specify this parameter only when ProductForm is set to IntegrationForm.
        self.reserved_node_size = reserved_node_size
        # The reserved storage resources. Valid values: 0 ACU to 2064 ACU. Step: 24. 1 ACU is approximately equal to 1 core and 4 GB of memory.
        # > Include the unit when you specify this parameter.
        self.storage_resource = storage_resource

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ainode_number is not None:
            result['AINodeNumber'] = self.ainode_number

        if self.ainode_spec is not None:
            result['AINodeSpec'] = self.ainode_spec

        if self.compute_resource is not None:
            result['ComputeResource'] = self.compute_resource

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.enable_default_resource_pool is not None:
            result['EnableDefaultResourcePool'] = self.enable_default_resource_pool

        if self.product_form is not None:
            result['ProductForm'] = self.product_form

        if self.product_version is not None:
            result['ProductVersion'] = self.product_version

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
        if m.get('AINodeNumber') is not None:
            self.ainode_number = m.get('AINodeNumber')

        if m.get('AINodeSpec') is not None:
            self.ainode_spec = m.get('AINodeSpec')

        if m.get('ComputeResource') is not None:
            self.compute_resource = m.get('ComputeResource')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EnableDefaultResourcePool') is not None:
            self.enable_default_resource_pool = m.get('EnableDefaultResourcePool')

        if m.get('ProductForm') is not None:
            self.product_form = m.get('ProductForm')

        if m.get('ProductVersion') is not None:
            self.product_version = m.get('ProductVersion')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReservedNodeCount') is not None:
            self.reserved_node_count = m.get('ReservedNodeCount')

        if m.get('ReservedNodeSize') is not None:
            self.reserved_node_size = m.get('ReservedNodeSize')

        if m.get('StorageResource') is not None:
            self.storage_resource = m.get('StorageResource')

        return self

