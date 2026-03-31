# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCloudResourceAccessPortDetailsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        port: str = None,
        protocol: str = None,
        region_id: str = None,
        resource_instance_id: str = None,
        resource_manager_resource_group_id: str = None,
        resource_product: str = None,
    ):
        # The ID of the WAF instance.
        # 
        # >  You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Default value: **10**.
        self.page_size = page_size
        # The port of the cloud service that is added to WAF.
        self.port = port
        # The type of the protocol. Valid values:
        # 
        # *   **http**
        # *   **https**
        self.protocol = protocol
        # The region in which the WAF instance is deployed. Valid values:
        # 
        # *   **cn-hangzhou**: the Chinese mainland.
        # *   **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The instance ID of the resource.
        # 
        # This parameter is required.
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.port is not None:
            result['Port'] = self.port

        if self.protocol is not None:
            result['Protocol'] = self.protocol

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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceInstanceId') is not None:
            self.resource_instance_id = m.get('ResourceInstanceId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('ResourceProduct') is not None:
            self.resource_product = m.get('ResourceProduct')

        return self

