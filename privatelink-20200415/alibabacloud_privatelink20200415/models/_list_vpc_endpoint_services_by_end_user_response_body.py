# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_privatelink20200415 import models as main_models
from darabonba.model import DaraModel

class ListVpcEndpointServicesByEndUserResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        services: List[main_models.ListVpcEndpointServicesByEndUserResponseBodyServices] = None,
        total_count: str = None,
    ):
        # The number of entries returned per page.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results. Valid values:
        # 
        # - If this parameter is empty, all results have been returned.
        # 
        # - If a value is returned, use it in a subsequent request to retrieve the next page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The endpoint services.
        self.services = services
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.services:
            for v1 in self.services:
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

        result['Services'] = []
        if self.services is not None:
            for k1 in self.services:
                result['Services'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.services = []
        if m.get('Services') is not None:
            for k1 in m.get('Services'):
                temp_model = main_models.ListVpcEndpointServicesByEndUserResponseBodyServices()
                self.services.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListVpcEndpointServicesByEndUserResponseBodyServices(DaraModel):
    def __init__(
        self,
        address_ip_version: str = None,
        auto_accept_enabled: bool = None,
        payer: str = None,
        resource_group_id: str = None,
        service_domain: str = None,
        service_id: str = None,
        service_name: str = None,
        service_resource_type: str = None,
        service_support_ipv_6: bool = None,
        service_type: str = None,
        tags: List[main_models.ListVpcEndpointServicesByEndUserResponseBodyServicesTags] = None,
        vpc_endpoint_policy_supported: bool = None,
        zone_affinity_enabled: bool = None,
        zones: List[str] = None,
    ):
        # The IP version. Valid values:
        # 
        # - **IPv4**: The service supports IPv4.
        # 
        # - **DualStack**: The service supports both IPv4 and IPv6 (dual stack).
        self.address_ip_version = address_ip_version
        # Specifies whether connection requests are automatically accepted. Valid values:
        # 
        # - **true**: Connection requests are automatically accepted.
        # 
        # - **false**: Connection requests must be manually accepted.
        self.auto_accept_enabled = auto_accept_enabled
        # The payer. Valid values:
        # 
        # - **Endpoint**: the service consumer.
        # 
        # - **EndpointService**: the service provider.
        self.payer = payer
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The domain name of the endpoint service.
        self.service_domain = service_domain
        # The ID of the endpoint service.
        self.service_id = service_id
        # The name of the endpoint service.
        self.service_name = service_name
        # The service resource type.
        # 
        # - **slb**: A Classic Load Balancer (CLB) instance.
        # 
        # - **alb**: An Application Load Balancer (ALB) instance.
        # 
        # - **nlb**: A Network Load Balancer (NLB) instance.
        self.service_resource_type = service_resource_type
        # Specifies whether the endpoint service supports IPv6. Valid values:
        # 
        # - **true**: The endpoint service supports IPv6.
        # 
        # - **false**: The endpoint service does not support IPv6.
        self.service_support_ipv_6 = service_support_ipv_6
        # The type of the endpoint service.
        # 
        # The value is always **Interface**. This indicates an interface endpoint where you can add service resources such as Application Load Balancer (ALB), Classic Load Balancer (CLB), and Network Load Balancer (NLB).
        self.service_type = service_type
        # A list of tags.
        self.tags = tags
        self.vpc_endpoint_policy_supported = vpc_endpoint_policy_supported
        # Specifies whether zone affinity is enabled. Valid values:
        # 
        # - **true**: Zone affinity is enabled.
        # 
        # - **false**: Zone affinity is disabled.
        self.zone_affinity_enabled = zone_affinity_enabled
        # The zones where the endpoint service is available.
        self.zones = zones

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_ip_version is not None:
            result['AddressIpVersion'] = self.address_ip_version

        if self.auto_accept_enabled is not None:
            result['AutoAcceptEnabled'] = self.auto_accept_enabled

        if self.payer is not None:
            result['Payer'] = self.payer

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.service_domain is not None:
            result['ServiceDomain'] = self.service_domain

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.service_resource_type is not None:
            result['ServiceResourceType'] = self.service_resource_type

        if self.service_support_ipv_6 is not None:
            result['ServiceSupportIPv6'] = self.service_support_ipv_6

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.vpc_endpoint_policy_supported is not None:
            result['VpcEndpointPolicySupported'] = self.vpc_endpoint_policy_supported

        if self.zone_affinity_enabled is not None:
            result['ZoneAffinityEnabled'] = self.zone_affinity_enabled

        if self.zones is not None:
            result['Zones'] = self.zones

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressIpVersion') is not None:
            self.address_ip_version = m.get('AddressIpVersion')

        if m.get('AutoAcceptEnabled') is not None:
            self.auto_accept_enabled = m.get('AutoAcceptEnabled')

        if m.get('Payer') is not None:
            self.payer = m.get('Payer')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ServiceDomain') is not None:
            self.service_domain = m.get('ServiceDomain')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('ServiceResourceType') is not None:
            self.service_resource_type = m.get('ServiceResourceType')

        if m.get('ServiceSupportIPv6') is not None:
            self.service_support_ipv_6 = m.get('ServiceSupportIPv6')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListVpcEndpointServicesByEndUserResponseBodyServicesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VpcEndpointPolicySupported') is not None:
            self.vpc_endpoint_policy_supported = m.get('VpcEndpointPolicySupported')

        if m.get('ZoneAffinityEnabled') is not None:
            self.zone_affinity_enabled = m.get('ZoneAffinityEnabled')

        if m.get('Zones') is not None:
            self.zones = m.get('Zones')

        return self

class ListVpcEndpointServicesByEndUserResponseBodyServicesTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

