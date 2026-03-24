# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCloudResourceListRequest(DaraModel):
    def __init__(
        self,
        cloud_resource_id: str = None,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
        owner_user_id: str = None,
        port: str = None,
        region_id: str = None,
        resource_instance_id: str = None,
        resource_manager_resource_group_id: str = None,
        resource_product: str = None,
    ):
        # The ID of the protected resource. WAF automatically generates this ID when you add the resource to WAF.
        # 
        # > Call [CreateCloudResource](https://help.aliyun.com/document_detail/2839876.html) to add a resource. Then, view the resource ID in the response.
        self.cloud_resource_id = cloud_resource_id
        # The ID of the WAF instance.
        # 
        # > Call [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of entries to return on each page. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results. You do not need to specify this parameter for the first request.
        # 
        # > If a value is returned for this parameter, it indicates that a next page is available. To retrieve the next page of data, include the returned **NextToken** in your next request. Repeat this process until no value is returned, which indicates that all data has been retrieved.
        self.next_token = next_token
        # The ID of the Alibaba Cloud account to which the resource belongs.
        self.owner_user_id = owner_user_id
        # The port of the cloud service that is added to WAF.
        self.port = port
        # The region where the WAF instance resides. Valid values:
        # 
        # - **cn-hangzhou**: the Chinese mainland.
        # 
        # - **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the resource instance.
        self.resource_instance_id = resource_instance_id
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The cloud service to which the resource belongs. Valid values:
        # 
        # - **alb**: Application Load Balancer (ALB).
        # 
        # - **mse**: Microservices Engine (MSE).
        # 
        # - **fc**: Function Compute (FC).
        # 
        # - **sae**: Serverless App Engine (SAE).
        # 
        # - **ecs**: Elastic Compute Service (ECS).
        # 
        # - **clb4**: Classic Load Balancer (CLB) that uses the TCP protocol.
        # 
        # - **clb7**: CLB that uses the HTTP or HTTPS protocol.
        # 
        # - **apig**: API Gateway (APIG).
        # 
        # - **nlb**: Network Load Balancer (NLB).
        # 
        # > Not all cloud services are available in all regions. If you specify this parameter, make sure that the specified cloud service is available in the selected region. Otherwise, the request may fail.
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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id

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

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')

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

