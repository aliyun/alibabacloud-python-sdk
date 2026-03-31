# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteCloudResourceRequest(DaraModel):
    def __init__(
        self,
        cloud_resource_id: str = None,
        instance_id: str = None,
        port: int = None,
        region_id: str = None,
        resource_instance_id: str = None,
        resource_manager_resource_group_id: str = None,
        resource_product: str = None,
    ):
        self.cloud_resource_id = cloud_resource_id
        # The ID of the WAF instance.
        # 
        # >  You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The port of the resource that is added to WAF.
        self.port = port
        # The region in which the WAF instance is deployed. Valid values:
        # 
        # *   **cn-hangzhou**: the Chinese mainland.
        # *   **ap-southeast-1**: outside the Chinese mainland.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the instance.
        self.resource_instance_id = resource_instance_id
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The cloud service. Valid values:
        # 
        # *   **clb4**: Layer 4 CLB.
        # *   **clb7**: Layer 7 CLB.
        # *   **ecs**: ECS.
        self.resource_product = resource_product

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_resource_id is not None:
            result['CloudResourceId'] = self.cloud_resource_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.port is not None:
            result['Port'] = self.port

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_instance_id is not None:
            result['ResourceInstanceId'] = self.resource_instance_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.resource_product is not None:
            result['ResourceProduct'] = self.resource_product

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudResourceId') is not None:
            self.cloud_resource_id = m.get('CloudResourceId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceInstanceId') is not None:
            self.resource_instance_id = m.get('ResourceInstanceId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('ResourceProduct') is not None:
            self.resource_product = m.get('ResourceProduct')

        return self

