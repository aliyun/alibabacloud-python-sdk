# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCloudResourcesRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        owner_user_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_domain: str = None,
        resource_function: str = None,
        resource_instance_id: str = None,
        resource_instance_name: str = None,
        resource_manager_resource_group_id: str = None,
        resource_name: str = None,
        resource_product: str = None,
        resource_region_id: str = None,
        resource_route_name: str = None,
    ):
        # The ID of the WAF instance.
        # 
        # > Call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The UID of the account to which the resource belongs.
        self.owner_user_id = owner_user_id
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Default value: **10**.
        self.page_size = page_size
        # The region where the WAF instance resides. Valid values:
        # 
        # - **cn-hangzhou**: the Chinese mainland.
        # 
        # - **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The domain name of the resource. This parameter is available when you query FC or SAE resources.
        self.resource_domain = resource_domain
        # The name of the function. This parameter is available when you query FC resources.
        self.resource_function = resource_function
        # The ID of the resource instance.
        self.resource_instance_id = resource_instance_id
        # The name of the instance that is added to WAF.
        self.resource_instance_name = resource_instance_name
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The name of the resource instance.
        self.resource_name = resource_name
        # The cloud service to which the resource belongs. By default, instances of Application Load Balancer (ALB), Microservices Engine (MSE), Function Compute (FC), and Serverless App Engine (SAE) are returned. Valid values:
        # 
        # - **alb**: ALB
        # 
        # - **mse**: MSE
        # 
        # - **fc**: FC
        # 
        # - **sae**: SAE
        # 
        # - **ecs**: Elastic Compute Service (ECS)
        # 
        # - **clb4**: Classic Load Balancer (CLB) that uses TCP
        # 
        # - **clb7**: CLB that uses HTTP or HTTPS
        # 
        # - **nlb**: Network Load Balancer (NLB)
        # 
        # > Each cloud service supports different regions. If you specify this parameter, make sure the region you specify for the ResourceRegionId parameter supports this service. Otherwise, the query may fail.
        self.resource_product = resource_product
        # The ID of the region where the resource resides. For more information, see the "Regions and supported products" section in this topic.
        # 
        # > Each cloud service supports different regions. If you specify the ResourceProduct parameter, make sure the region you specify for this parameter supports that service. Otherwise, the query may fail.
        self.resource_region_id = resource_region_id
        # The name of the route. This parameter is available when you query MSE resources.
        self.resource_route_name = resource_route_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_domain is not None:
            result['ResourceDomain'] = self.resource_domain

        if self.resource_function is not None:
            result['ResourceFunction'] = self.resource_function

        if self.resource_instance_id is not None:
            result['ResourceInstanceId'] = self.resource_instance_id

        if self.resource_instance_name is not None:
            result['ResourceInstanceName'] = self.resource_instance_name

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.resource_product is not None:
            result['ResourceProduct'] = self.resource_product

        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id

        if self.resource_route_name is not None:
            result['ResourceRouteName'] = self.resource_route_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceDomain') is not None:
            self.resource_domain = m.get('ResourceDomain')

        if m.get('ResourceFunction') is not None:
            self.resource_function = m.get('ResourceFunction')

        if m.get('ResourceInstanceId') is not None:
            self.resource_instance_id = m.get('ResourceInstanceId')

        if m.get('ResourceInstanceName') is not None:
            self.resource_instance_name = m.get('ResourceInstanceName')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ResourceProduct') is not None:
            self.resource_product = m.get('ResourceProduct')

        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')

        if m.get('ResourceRouteName') is not None:
            self.resource_route_name = m.get('ResourceRouteName')

        return self

