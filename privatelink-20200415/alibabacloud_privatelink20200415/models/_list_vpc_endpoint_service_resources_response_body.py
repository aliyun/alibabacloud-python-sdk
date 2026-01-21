# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_privatelink20200415 import models as main_models
from darabonba.model import DaraModel

class ListVpcEndpointServiceResourcesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        resources: List[main_models.ListVpcEndpointServiceResourcesResponseBodyResources] = None,
    ):
        # The number of entries returned on each page.
        self.max_results = max_results
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If no value is returned for **NextToken**, no next requests are performed.
        # *   If a value is returned for **NextToken**, the value can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The service resources.
        self.resources = resources

    def validate(self):
        if self.resources:
            for v1 in self.resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['Resources'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resources = []
        if m.get('Resources') is not None:
            for k1 in m.get('Resources'):
                temp_model = main_models.ListVpcEndpointServiceResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k1))

        return self

class ListVpcEndpointServiceResourcesResponseBodyResources(DaraModel):
    def __init__(
        self,
        auto_allocated_enabled: bool = None,
        ip: str = None,
        region_id: str = None,
        related_deprecated_endpoint_count: int = None,
        related_endpoint_count: int = None,
        resource_id: str = None,
        resource_support_ipv_6: bool = None,
        resource_type: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # Indicates whether automatic resource allocation is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.auto_allocated_enabled = auto_allocated_enabled
        # The IP address of the service resource.
        self.ip = ip
        # The ID of the region where the service resource is deployed.
        self.region_id = region_id
        # The number of endpoints that are associated with the service resource that is smoothly migrated.
        self.related_deprecated_endpoint_count = related_deprecated_endpoint_count
        # The number of endpoints that are associated with the service resource.
        self.related_endpoint_count = related_endpoint_count
        # The service resource ID.
        self.resource_id = resource_id
        # Indicates whether IPv6 is enabled for the endpoint service. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.resource_support_ipv_6 = resource_support_ipv_6
        # The type of the service resource.
        # 
        # Only **slb** is returned. This value indicates a Classic Load Balancer (CLB) instance.
        self.resource_type = resource_type
        # The ID of the vSwitch to which the service resource belongs.
        self.v_switch_id = v_switch_id
        # The ID of the virtual private cloud (VPC) to which the service resource belongs.
        self.vpc_id = vpc_id
        # The ID of the zone to which the service resource belongs.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_allocated_enabled is not None:
            result['AutoAllocatedEnabled'] = self.auto_allocated_enabled

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.related_deprecated_endpoint_count is not None:
            result['RelatedDeprecatedEndpointCount'] = self.related_deprecated_endpoint_count

        if self.related_endpoint_count is not None:
            result['RelatedEndpointCount'] = self.related_endpoint_count

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_support_ipv_6 is not None:
            result['ResourceSupportIPv6'] = self.resource_support_ipv_6

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoAllocatedEnabled') is not None:
            self.auto_allocated_enabled = m.get('AutoAllocatedEnabled')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RelatedDeprecatedEndpointCount') is not None:
            self.related_deprecated_endpoint_count = m.get('RelatedDeprecatedEndpointCount')

        if m.get('RelatedEndpointCount') is not None:
            self.related_endpoint_count = m.get('RelatedEndpointCount')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceSupportIPv6') is not None:
            self.resource_support_ipv_6 = m.get('ResourceSupportIPv6')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

