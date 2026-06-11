# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_privatelink20200415 import models as main_models
from darabonba.model import DaraModel

class CreateVpcEndpointServiceResponseBody(DaraModel):
    def __init__(
        self,
        address_ip_version: str = None,
        auto_accept_enabled: bool = None,
        create_time: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        service_business_status: str = None,
        service_description: str = None,
        service_domain: str = None,
        service_id: str = None,
        service_name: str = None,
        service_status: str = None,
        service_support_ipv_6: bool = None,
        supported_region_set: List[main_models.CreateVpcEndpointServiceResponseBodySupportedRegionSet] = None,
        zone_affinity_enabled: bool = None,
    ):
        # The IP version. Valid values:
        # 
        # - **IPv4**: IPv4.
        # - **DualStack**: dual stack.
        self.address_ip_version = address_ip_version
        # Indicates whether endpoint connection requests are automatically accepted. Valid values:
        # 
        # - **true**: automatically accepts endpoint connection requests.
        # - **false**: does not automatically accept endpoint connection requests.
        self.auto_accept_enabled = auto_accept_enabled
        # The time when the endpoint service was created.
        self.create_time = create_time
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The business status of the endpoint service. Valid values:
        # 
        # - **Normal**: normal.
        # 
        # - **FinancialLocked**: locked due to overdue payments.
        self.service_business_status = service_business_status
        # The description of the endpoint service.
        self.service_description = service_description
        # The domain name of the endpoint service.
        self.service_domain = service_domain
        # The ID of the endpoint service.
        self.service_id = service_id
        # The name of the endpoint service.
        self.service_name = service_name
        # The state of the endpoint service. Valid values:
        # 
        # - **Creating**: being created.
        # 
        # - **Pending**: being modified.
        # 
        # - **Active**: available.
        # 
        # - **Deleting**: being deleted.
        self.service_status = service_status
        # Indicates whether the endpoint service supports IPv6. Valid values:
        # 
        # - **true**: yes.
        # 
        # - **false**: no.
        self.service_support_ipv_6 = service_support_ipv_6
        # The list of regions in which the endpoint service is available. Service consumers can initiate endpoint connections from the regions in the list.
        self.supported_region_set = supported_region_set
        # Indicates whether zone affinity is enabled for endpoint domain name resolution. Valid values:
        # 
        # - **true**: yes.
        # - **false**: no.
        self.zone_affinity_enabled = zone_affinity_enabled

    def validate(self):
        if self.supported_region_set:
            for v1 in self.supported_region_set:
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

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status

        if self.service_support_ipv_6 is not None:
            result['ServiceSupportIPv6'] = self.service_support_ipv_6

        result['SupportedRegionSet'] = []
        if self.supported_region_set is not None:
            for k1 in self.supported_region_set:
                result['SupportedRegionSet'].append(k1.to_map() if k1 else None)

        if self.zone_affinity_enabled is not None:
            result['ZoneAffinityEnabled'] = self.zone_affinity_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressIpVersion') is not None:
            self.address_ip_version = m.get('AddressIpVersion')

        if m.get('AutoAcceptEnabled') is not None:
            self.auto_accept_enabled = m.get('AutoAcceptEnabled')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

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

        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')

        if m.get('ServiceSupportIPv6') is not None:
            self.service_support_ipv_6 = m.get('ServiceSupportIPv6')

        self.supported_region_set = []
        if m.get('SupportedRegionSet') is not None:
            for k1 in m.get('SupportedRegionSet'):
                temp_model = main_models.CreateVpcEndpointServiceResponseBodySupportedRegionSet()
                self.supported_region_set.append(temp_model.from_map(k1))

        if m.get('ZoneAffinityEnabled') is not None:
            self.zone_affinity_enabled = m.get('ZoneAffinityEnabled')

        return self

class CreateVpcEndpointServiceResponseBodySupportedRegionSet(DaraModel):
    def __init__(
        self,
        region_business_status: str = None,
        region_service_status: str = None,
        service_region_id: str = None,
        supported_region_id: str = None,
    ):
        # The business status of the region in which the endpoint service is available. Valid values:
        # 
        # - **Normal**: normal.
        # - **FinancialLocked**: locked due to overdue payments.
        self.region_business_status = region_business_status
        # The state of the region in which the endpoint service is available. Valid values:
        # 
        # - **Pending**: changing.
        # - **Available**: available.
        # - **Deleting**: being deleted.
        # - **Failed**: failed.
        # - **Closed**: closed.
        self.region_service_status = region_service_status
        self.service_region_id = service_region_id
        # The ID of a region in which the endpoint service is available.
        self.supported_region_id = supported_region_id

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

        if self.supported_region_id is not None:
            result['SupportedRegionId'] = self.supported_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionBusinessStatus') is not None:
            self.region_business_status = m.get('RegionBusinessStatus')

        if m.get('RegionServiceStatus') is not None:
            self.region_service_status = m.get('RegionServiceStatus')

        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')

        if m.get('SupportedRegionId') is not None:
            self.supported_region_id = m.get('SupportedRegionId')

        return self

