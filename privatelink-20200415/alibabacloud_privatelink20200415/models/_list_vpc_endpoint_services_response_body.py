# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_privatelink20200415 import models as main_models
from darabonba.model import DaraModel

class ListVpcEndpointServicesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        services: List[main_models.ListVpcEndpointServicesResponseBodyServices] = None,
        total_count: int = None,
    ):
        # The number of entries returned per page.
        self.max_results = max_results
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If no value is returned for **NextToken**, no next requests are performed.
        # *   If a value is returned for **NextToken**, the value can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The endpoint services.
        self.services = services
        # The total number of entries returned.
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
                temp_model = main_models.ListVpcEndpointServicesResponseBodyServices()
                self.services.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListVpcEndpointServicesResponseBodyServices(DaraModel):
    def __init__(
        self,
        address_ip_version: str = None,
        auto_accept_enabled: bool = None,
        connect_bandwidth: int = None,
        create_time: str = None,
        max_bandwidth: int = None,
        min_bandwidth: int = None,
        payer: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        service_business_status: str = None,
        service_description: str = None,
        service_domain: str = None,
        service_id: str = None,
        service_name: str = None,
        service_resource_type: str = None,
        service_status: str = None,
        service_support_ipv_6: bool = None,
        service_type: str = None,
        supported_region_set: List[main_models.ListVpcEndpointServicesResponseBodyServicesSupportedRegionSet] = None,
        tags: List[main_models.ListVpcEndpointServicesResponseBodyServicesTags] = None,
        zone_affinity_enabled: bool = None,
    ):
        # The protocol. Valid values:
        # 
        # *   **IPv4**
        # *   **DualStack**
        self.address_ip_version = address_ip_version
        # Indicates whether endpoint connection requests are automatically accepted. Valid values:
        # 
        # *   **true**: Endpoint connection requests are automatically accepted.
        # *   **false**: Endpoint connection requests are not automatically accepted.
        self.auto_accept_enabled = auto_accept_enabled
        # The default maximum bandwidth of the endpoint connection. Unit: Mbit/s.
        self.connect_bandwidth = connect_bandwidth
        # The time when the endpoint service was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The maximum bandwidth of the endpoint connection. Unit: Mbit/s.
        self.max_bandwidth = max_bandwidth
        # The minimum bandwidth of the endpoint connection. Unit: Mbit/s.
        self.min_bandwidth = min_bandwidth
        # The payer. Valid values:
        # 
        # *   **Endpoint**: service consumer
        # *   **EndpointService**: service provider
        self.payer = payer
        # The region ID of the endpoint service.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The service state of the endpoint service. Valid values:
        # 
        # *   **Normal**: The endpoint service runs as expected.
        # *   **FinancialLocked**: The endpoint service is locked due to overdue payments.
        self.service_business_status = service_business_status
        # The description of the endpoint service.
        self.service_description = service_description
        # The domain name of the endpoint service.
        self.service_domain = service_domain
        # The ID of the endpoint service.
        self.service_id = service_id
        # The name of the endpoint service.
        self.service_name = service_name
        # The type of the service resource. Valid values:
        # 
        # *   **slb**: Classic Load Balancer (CLB) instance
        # *   **alb**: Application Load Balancer (ALB) instance
        # *   **nlb**: Network Load Balancer (NLB) instance
        self.service_resource_type = service_resource_type
        # The state of the endpoint service. Valid values:
        # 
        # *   **Creating**: The endpoint service is being created.
        # *   **Pending**: The endpoint service is being modified.
        # *   **Active**: The endpoint service is available.
        # *   **Deleting**: The endpoint service is being deleted.
        self.service_status = service_status
        # Indicates whether the endpoint service supports IPv6. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.service_support_ipv_6 = service_support_ipv_6
        # The type of the endpoint service.
        # 
        # *   Only **Interface** may be returned. You can specify CLB, ALB, and NLB instances as the service resources of the endpoint service.
        self.service_type = service_type
        self.supported_region_set = supported_region_set
        # The tags added to the resource.
        self.tags = tags
        # Indicates whether zone affinity is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.zone_affinity_enabled = zone_affinity_enabled

    def validate(self):
        if self.supported_region_set:
            for v1 in self.supported_region_set:
                 if v1:
                    v1.validate()
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

        if self.connect_bandwidth is not None:
            result['ConnectBandwidth'] = self.connect_bandwidth

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.max_bandwidth is not None:
            result['MaxBandwidth'] = self.max_bandwidth

        if self.min_bandwidth is not None:
            result['MinBandwidth'] = self.min_bandwidth

        if self.payer is not None:
            result['Payer'] = self.payer

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.service_business_status is not None:
            result['ServiceBusinessStatus'] = self.service_business_status

        if self.service_description is not None:
            result['ServiceDescription'] = self.service_description

        if self.service_domain is not None:
            result['ServiceDomain'] = self.service_domain

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.service_resource_type is not None:
            result['ServiceResourceType'] = self.service_resource_type

        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status

        if self.service_support_ipv_6 is not None:
            result['ServiceSupportIPv6'] = self.service_support_ipv_6

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        result['SupportedRegionSet'] = []
        if self.supported_region_set is not None:
            for k1 in self.supported_region_set:
                result['SupportedRegionSet'].append(k1.to_map() if k1 else None)

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.zone_affinity_enabled is not None:
            result['ZoneAffinityEnabled'] = self.zone_affinity_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressIpVersion') is not None:
            self.address_ip_version = m.get('AddressIpVersion')

        if m.get('AutoAcceptEnabled') is not None:
            self.auto_accept_enabled = m.get('AutoAcceptEnabled')

        if m.get('ConnectBandwidth') is not None:
            self.connect_bandwidth = m.get('ConnectBandwidth')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('MaxBandwidth') is not None:
            self.max_bandwidth = m.get('MaxBandwidth')

        if m.get('MinBandwidth') is not None:
            self.min_bandwidth = m.get('MinBandwidth')

        if m.get('Payer') is not None:
            self.payer = m.get('Payer')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ServiceBusinessStatus') is not None:
            self.service_business_status = m.get('ServiceBusinessStatus')

        if m.get('ServiceDescription') is not None:
            self.service_description = m.get('ServiceDescription')

        if m.get('ServiceDomain') is not None:
            self.service_domain = m.get('ServiceDomain')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('ServiceResourceType') is not None:
            self.service_resource_type = m.get('ServiceResourceType')

        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')

        if m.get('ServiceSupportIPv6') is not None:
            self.service_support_ipv_6 = m.get('ServiceSupportIPv6')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        self.supported_region_set = []
        if m.get('SupportedRegionSet') is not None:
            for k1 in m.get('SupportedRegionSet'):
                temp_model = main_models.ListVpcEndpointServicesResponseBodyServicesSupportedRegionSet()
                self.supported_region_set.append(temp_model.from_map(k1))

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListVpcEndpointServicesResponseBodyServicesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('ZoneAffinityEnabled') is not None:
            self.zone_affinity_enabled = m.get('ZoneAffinityEnabled')

        return self

class ListVpcEndpointServicesResponseBodyServicesTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag added to the resource.
        self.key = key
        # The value of the tag added to the resource.
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

class ListVpcEndpointServicesResponseBodyServicesSupportedRegionSet(DaraModel):
    def __init__(
        self,
        region_business_status: str = None,
        region_service_status: str = None,
        service_region_id: str = None,
    ):
        self.region_business_status = region_business_status
        self.region_service_status = region_service_status
        self.service_region_id = service_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_business_status is not None:
            result['RegionBusinessStatus'] = self.region_business_status

        if self.region_service_status is not None:
            result['RegionServiceStatus'] = self.region_service_status

        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionBusinessStatus') is not None:
            self.region_business_status = m.get('RegionBusinessStatus')

        if m.get('RegionServiceStatus') is not None:
            self.region_service_status = m.get('RegionServiceStatus')

        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')

        return self

