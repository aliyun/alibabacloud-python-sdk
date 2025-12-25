# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudResourcesResponseBody(DaraModel):
    def __init__(
        self,
        cloud_resources: List[main_models.DescribeCloudResourcesResponseBodyCloudResources] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The cloud service resources that are added to WAF.
        self.cloud_resources = cloud_resources
        # The request ID.
        self.request_id = request_id
        # The total number of cloud service resources returned.
        self.total_count = total_count

    def validate(self):
        if self.cloud_resources:
            for v1 in self.cloud_resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CloudResources'] = []
        if self.cloud_resources is not None:
            for k1 in self.cloud_resources:
                result['CloudResources'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cloud_resources = []
        if m.get('CloudResources') is not None:
            for k1 in m.get('CloudResources'):
                temp_model = main_models.DescribeCloudResourcesResponseBodyCloudResources()
                self.cloud_resources.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCloudResourcesResponseBodyCloudResources(DaraModel):
    def __init__(
        self,
        http_port_count: int = None,
        https_port_count: int = None,
        owner_user_id: str = None,
        resource_domain: str = None,
        resource_function: str = None,
        resource_instance: str = None,
        resource_instance_id: str = None,
        resource_instance_ip: str = None,
        resource_instance_name: str = None,
        resource_name: str = None,
        resource_product: str = None,
        resource_region_id: str = None,
        resource_route_name: str = None,
        resource_service: str = None,
    ):
        # The number of the HTTP ports that are added to WAF.
        # 
        # >  This parameter is returned only if the cloud service is ECS or CLB.
        self.http_port_count = http_port_count
        # The number of the HTTPS ports that are added to WAF.
        # 
        # >  This parameter is returned only if the cloud service is ECS or CLB.
        self.https_port_count = https_port_count
        # The ID of the Alibaba Cloud account to which the resource belongs.
        self.owner_user_id = owner_user_id
        # The domain name. This parameter has a value only if the value of ResourceProduct is fc or sae.
        self.resource_domain = resource_domain
        # The function name. This parameter has a value only if the value of ResourceProduct is fc.
        self.resource_function = resource_function
        # The ID of the resource.
        self.resource_instance = resource_instance
        # The ID of the instance that is added to WAF.
        self.resource_instance_id = resource_instance_id
        # The IP address of the instance that is added to WAF.
        self.resource_instance_ip = resource_instance_ip
        # The name of the instance that is added to WAF.
        self.resource_instance_name = resource_instance_name
        # The name of the resource.
        self.resource_name = resource_name
        # The cloud service to which the resource belongs. Valid values:
        # 
        # *   **alb**: ALB.
        # *   **mse**: MSE.
        # *   **fc**: Function Compute.
        # *   **sae**: SAE.
        # *   **ecs**: ECS.
        # *   **clb4**: Layer 4 CLB.
        # *   **clb7**: Layer 7 CLB.
        self.resource_product = resource_product
        # The region ID of the resource.
        self.resource_region_id = resource_region_id
        # The route name. This parameter has a value only if the value of ResourceProduct is mse.
        self.resource_route_name = resource_route_name
        # The service name. This parameter has a value only if the value of ResourceProduct is fc.
        self.resource_service = resource_service

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.http_port_count is not None:
            result['HttpPortCount'] = self.http_port_count

        if self.https_port_count is not None:
            result['HttpsPortCount'] = self.https_port_count

        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id

        if self.resource_domain is not None:
            result['ResourceDomain'] = self.resource_domain

        if self.resource_function is not None:
            result['ResourceFunction'] = self.resource_function

        if self.resource_instance is not None:
            result['ResourceInstance'] = self.resource_instance

        if self.resource_instance_id is not None:
            result['ResourceInstanceId'] = self.resource_instance_id

        if self.resource_instance_ip is not None:
            result['ResourceInstanceIp'] = self.resource_instance_ip

        if self.resource_instance_name is not None:
            result['ResourceInstanceName'] = self.resource_instance_name

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.resource_product is not None:
            result['ResourceProduct'] = self.resource_product

        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id

        if self.resource_route_name is not None:
            result['ResourceRouteName'] = self.resource_route_name

        if self.resource_service is not None:
            result['ResourceService'] = self.resource_service

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpPortCount') is not None:
            self.http_port_count = m.get('HttpPortCount')

        if m.get('HttpsPortCount') is not None:
            self.https_port_count = m.get('HttpsPortCount')

        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')

        if m.get('ResourceDomain') is not None:
            self.resource_domain = m.get('ResourceDomain')

        if m.get('ResourceFunction') is not None:
            self.resource_function = m.get('ResourceFunction')

        if m.get('ResourceInstance') is not None:
            self.resource_instance = m.get('ResourceInstance')

        if m.get('ResourceInstanceId') is not None:
            self.resource_instance_id = m.get('ResourceInstanceId')

        if m.get('ResourceInstanceIp') is not None:
            self.resource_instance_ip = m.get('ResourceInstanceIp')

        if m.get('ResourceInstanceName') is not None:
            self.resource_instance_name = m.get('ResourceInstanceName')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ResourceProduct') is not None:
            self.resource_product = m.get('ResourceProduct')

        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')

        if m.get('ResourceRouteName') is not None:
            self.resource_route_name = m.get('ResourceRouteName')

        if m.get('ResourceService') is not None:
            self.resource_service = m.get('ResourceService')

        return self

