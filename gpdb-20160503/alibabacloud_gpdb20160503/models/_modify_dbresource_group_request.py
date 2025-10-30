# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class ModifyDBResourceGroupRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        owner_id: int = None,
        resource_group_items: List[main_models.ModifyDBResourceGroupRequestResourceGroupItems] = None,
    ):
        # The instance ID.
        # 
        # >  You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.owner_id = owner_id
        # The information about the resource group.
        # 
        # This parameter is required.
        self.resource_group_items = resource_group_items

    def validate(self):
        if self.resource_group_items:
            for v1 in self.resource_group_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        result['ResourceGroupItems'] = []
        if self.resource_group_items is not None:
            for k1 in self.resource_group_items:
                result['ResourceGroupItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        self.resource_group_items = []
        if m.get('ResourceGroupItems') is not None:
            for k1 in m.get('ResourceGroupItems'):
                temp_model = main_models.ModifyDBResourceGroupRequestResourceGroupItems()
                self.resource_group_items.append(temp_model.from_map(k1))

        return self

class ModifyDBResourceGroupRequestResourceGroupItems(DaraModel):
    def __init__(
        self,
        resource_group_config: str = None,
        resource_group_name: str = None,
    ):
        # The configurations of the resource group to which you want to modify.
        # 
        # > 
        # 
        # *   CpuRateLimit: the percentage of CPU resources that are available for the resource group. Unit: %.
        # 
        # *   MemoryLimit: the percentage of memory resources that are available for the resource group. Unit: %.
        # 
        # *   MemorySharedQuota: the percentage of memory resources shared among transactions that are submitted to the resource group. Unit: %. Default value: 80.
        # 
        # *   MemorySpillRatio: the memory spill ratio for memory-intensive transactions. When the memory that is used by memory-intensive transactions reaches this value, data is spilled to disks. Unit: %. Default value: 0.
        # 
        # *   Concurrency: the maximum number of concurrent transactions or parallel queries that are allowed for a resource group. Default value: 20.
        # 
        # This parameter is required.
        self.resource_group_config = resource_group_config
        # The name of the resource group.
        # 
        # This parameter is required.
        self.resource_group_name = resource_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_group_config is not None:
            result['ResourceGroupConfig'] = self.resource_group_config

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupConfig') is not None:
            self.resource_group_config = m.get('ResourceGroupConfig')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        return self

