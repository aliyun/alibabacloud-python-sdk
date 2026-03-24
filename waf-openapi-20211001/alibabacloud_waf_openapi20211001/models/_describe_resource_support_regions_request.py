# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeResourceSupportRegionsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
        resource_product: str = None,
    ):
        # The ID of the WAF instance.
        # 
        # > You can call [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) to view the ID of the current WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region to which the WAF instance belongs. Valid values:
        # 
        # - **cn-hangzhou**: indicates the Chinese mainland.
        # 
        # - **ap-southeast-1**: indicates regions outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The cloud product to which the resource belongs. By default, instances of ALB, MSE, FC, and SAE products are returned. Valid values:
        # 
        # - **alb**: indicates the ALB product.
        # 
        # - **mse**: indicates the MSE product.
        # 
        # - **fc**: indicates the FC product.
        # 
        # - **sae**: indicates the SAE product.
        # 
        # - **ecs**: indicates the ECS product.
        # 
        # - **clb4**: indicates the CLB(TCP) product.
        # 
        # - **clb7**: indicates the CLB(HTTP/HTTPS) product.
        # 
        # - **apig**: indicates the APIG product.
        # 
        # - **nlb**: indicates the NLB product.
        # 
        # > Each product supports different regions. When the product filter field has a value, you need to refer to the regions supported by the product. Otherwise, the filtering may fail.
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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.resource_product is not None:
            result['ResourceProduct'] = self.resource_product

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('ResourceProduct') is not None:
            self.resource_product = m.get('ResourceProduct')

        return self

