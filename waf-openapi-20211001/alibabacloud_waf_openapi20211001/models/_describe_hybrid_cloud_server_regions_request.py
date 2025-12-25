# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHybridCloudServerRegionsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        region_code: str = None,
        region_id: str = None,
        region_type: str = None,
        resource_manager_resource_group_id: str = None,
    ):
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The code of the region.
        # 
        # >  This parameter is required if you set RegionType to region. The value is the code of the city.
        self.region_code = region_code
        # The region in which the WAF instance is deployed. Valid values:
        # 
        # *   **cn-hangzhou**: Chinese mainland.
        # *   **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The type of the region. Valid values:
        # 
        # *   **operator**: the ISP.
        # *   **continents**: the continent.
        # *   **region**: the city.
        # 
        # This parameter is required.
        self.region_type = region_type
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_code is not None:
            result['RegionCode'] = self.region_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.region_type is not None:
            result['RegionType'] = self.region_type

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RegionType') is not None:
            self.region_type = m.get('RegionType')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        return self

