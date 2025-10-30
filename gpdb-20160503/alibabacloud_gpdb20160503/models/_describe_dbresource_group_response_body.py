# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeDBResourceGroupResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_group_items: main_models.DescribeDBResourceGroupResponseBodyResourceGroupItems = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The queried resource group information.
        self.resource_group_items = resource_group_items

    def validate(self):
        if self.resource_group_items:
            self.resource_group_items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_items is not None:
            result['ResourceGroupItems'] = self.resource_group_items.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupItems') is not None:
            temp_model = main_models.DescribeDBResourceGroupResponseBodyResourceGroupItems()
            self.resource_group_items = temp_model.from_map(m.get('ResourceGroupItems'))

        return self

class DescribeDBResourceGroupResponseBodyResourceGroupItems(DaraModel):
    def __init__(
        self,
        resource_group_item: List[main_models.DescribeDBResourceGroupResponseBodyResourceGroupItemsResourceGroupItem] = None,
    ):
        self.resource_group_item = resource_group_item

    def validate(self):
        if self.resource_group_item:
            for v1 in self.resource_group_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ResourceGroupItem'] = []
        if self.resource_group_item is not None:
            for k1 in self.resource_group_item:
                result['ResourceGroupItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_group_item = []
        if m.get('ResourceGroupItem') is not None:
            for k1 in m.get('ResourceGroupItem'):
                temp_model = main_models.DescribeDBResourceGroupResponseBodyResourceGroupItemsResourceGroupItem()
                self.resource_group_item.append(temp_model.from_map(k1))

        return self

class DescribeDBResourceGroupResponseBodyResourceGroupItemsResourceGroupItem(DaraModel):
    def __init__(
        self,
        resource_group_config: str = None,
        resource_group_name: str = None,
        role_list: main_models.DescribeDBResourceGroupResponseBodyResourceGroupItemsResourceGroupItemRoleList = None,
    ):
        # The configurations of the resource group.
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
        self.resource_group_config = resource_group_config
        # The name of the resource group.
        self.resource_group_name = resource_group_name
        # The roles.
        self.role_list = role_list

    def validate(self):
        if self.role_list:
            self.role_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_group_config is not None:
            result['ResourceGroupConfig'] = self.resource_group_config

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        if self.role_list is not None:
            result['RoleList'] = self.role_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupConfig') is not None:
            self.resource_group_config = m.get('ResourceGroupConfig')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        if m.get('RoleList') is not None:
            temp_model = main_models.DescribeDBResourceGroupResponseBodyResourceGroupItemsResourceGroupItemRoleList()
            self.role_list = temp_model.from_map(m.get('RoleList'))

        return self

class DescribeDBResourceGroupResponseBodyResourceGroupItemsResourceGroupItemRoleList(DaraModel):
    def __init__(
        self,
        role: List[str] = None,
    ):
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.role is not None:
            result['Role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Role') is not None:
            self.role = m.get('Role')

        return self

