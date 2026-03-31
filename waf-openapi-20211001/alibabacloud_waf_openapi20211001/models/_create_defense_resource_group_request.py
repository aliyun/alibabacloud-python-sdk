# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDefenseResourceGroupRequest(DaraModel):
    def __init__(
        self,
        add_list: str = None,
        description: str = None,
        group_name: str = None,
        instance_id: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
    ):
        # The protected objects that you want to add to the protected object group. You can add multiple protected objects to a protected object group at the same time. You can specify multiple protected objects. Separate them with commas (,).
        self.add_list = add_list
        # The description of the protected object group.
        self.description = description
        # The name of the protected object group that you want to create.
        # 
        # This parameter is required.
        self.group_name = group_name
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to obtain the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region of the WAF instance. Valid values:
        # 
        # *   **cn-hangzhou**: Chinese mainland.
        # *   **ap-southeast-1**: Outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_list is not None:
            result['AddList'] = self.add_list

        if self.description is not None:
            result['Description'] = self.description

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddList') is not None:
            self.add_list = m.get('AddList')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        return self

