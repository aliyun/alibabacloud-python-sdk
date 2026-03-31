# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyHybridCloudServerRequest(DaraModel):
    def __init__(
        self,
        continents: str = None,
        custom_name: str = None,
        instance_id: str = None,
        mid: str = None,
        operator: str = None,
        region_code: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
    ):
        # The continent.
        # 
        # This parameter is required.
        self.continents = continents
        # The name of the node.
        # 
        # This parameter is required.
        self.custom_name = custom_name
        # The ID of the WAF instance.
        # 
        # >  You can call the [DescribeInstanceInfo](https://help.aliyun.com/document_detail/140857.html) operation to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the node.
        # 
        # This parameter is required.
        self.mid = mid
        # The cloud service provider.
        # 
        # This parameter is required.
        self.operator = operator
        # The city.
        # 
        # This parameter is required.
        self.region_code = region_code
        # The region of the WAF instance. Valid values:
        # 
        # *   **cn-hangzhou**: Chinese mainland.
        # *   **ap-southeast-1**: Outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.continents is not None:
            result['Continents'] = self.continents

        if self.custom_name is not None:
            result['CustomName'] = self.custom_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.mid is not None:
            result['Mid'] = self.mid

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.region_code is not None:
            result['RegionCode'] = self.region_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Continents') is not None:
            self.continents = m.get('Continents')

        if m.get('CustomName') is not None:
            self.custom_name = m.get('CustomName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Mid') is not None:
            self.mid = m.get('Mid')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        return self

