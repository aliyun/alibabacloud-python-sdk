# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_privatelink20200415 import models as main_models
from darabonba.model import DaraModel

class ListVpcEndpointServicesRequest(DaraModel):
    def __init__(
        self,
        address_ip_version: str = None,
        auto_accept_enabled: bool = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        service_business_status: str = None,
        service_id: str = None,
        service_name: str = None,
        service_resource_type: str = None,
        service_status: str = None,
        tag: List[main_models.ListVpcEndpointServicesRequestTag] = None,
        zone_affinity_enabled: bool = None,
    ):
        # The IP address version. Valid values:
        # 
        # - **IPv4**: IPv4 type.
        # 
        # - **DualStack**: Dual-stack type.
        self.address_ip_version = address_ip_version
        # Specifies whether to automatically accept endpoint connections. Valid values:
        # 
        # - **true**: Automatically accept endpoint connections.
        # 
        # - **false**: Do not automatically accept endpoint connections.
        self.auto_accept_enabled = auto_accept_enabled
        # The number of entries to return per page. Valid values: **1** to **1000**. Default value: **50**.
        self.max_results = max_results
        # A pagination token for the next query. Valid values:
        # 
        # - Leave this parameter empty for the first query or when no further results exist.
        # 
        # - If another query is needed, set this parameter to the NextToken value returned in the previous API call.
        self.next_token = next_token
        # The ID of the region where the endpoint service is deployed.
        # 
        # Call the [DescribeRegions](https://help.aliyun.com/document_detail/120468.html) operation to obtain the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the service resource.
        self.resource_id = resource_id
        # The business status of the endpoint service. Valid values:
        # 
        # - **Normal**: The endpoint service is running as expected.
        # 
        # - **FinancialLocked**: The endpoint service is locked due to an overdue payment.
        self.service_business_status = service_business_status
        # The ID of the endpoint service.
        self.service_id = service_id
        # The name of the endpoint service.
        self.service_name = service_name
        # The type of the service resource. Valid values:
        # 
        # - **slb**: The service resource is a Classic Load Balancer (CLB) instance.
        # 
        # - **alb**: The service resource is an Application Load Balancer (ALB) instance.
        # 
        # - **nlb**: The service resource is a Network Load Balancer (NLB) instance.
        # 
        # - **gwlb**: The service resource is a Gateway Load Balancer (GWLB) instance.
        self.service_resource_type = service_resource_type
        # The status of the endpoint service. Valid values:
        # 
        # - **Creating**: The endpoint service is being created.
        # 
        # - **Pending**: The endpoint service is being modified.
        # 
        # - **Active**: The endpoint service is available.
        # 
        # - **Deleting**: The endpoint service is being deleted.
        self.service_status = service_status
        # The list of tags.
        self.tag = tag
        # Specifies whether zonal affinity is enabled for domain name resolution. Valid values:
        # 
        # - **true**: Yes.
        # 
        # - **false**: No.
        self.zone_affinity_enabled = zone_affinity_enabled

    def validate(self):
        if self.tag:
            for v1 in self.tag:
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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.service_business_status is not None:
            result['ServiceBusinessStatus'] = self.service_business_status

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.service_resource_type is not None:
            result['ServiceResourceType'] = self.service_resource_type

        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.zone_affinity_enabled is not None:
            result['ZoneAffinityEnabled'] = self.zone_affinity_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressIpVersion') is not None:
            self.address_ip_version = m.get('AddressIpVersion')

        if m.get('AutoAcceptEnabled') is not None:
            self.auto_accept_enabled = m.get('AutoAcceptEnabled')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ServiceBusinessStatus') is not None:
            self.service_business_status = m.get('ServiceBusinessStatus')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('ServiceResourceType') is not None:
            self.service_resource_type = m.get('ServiceResourceType')

        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListVpcEndpointServicesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('ZoneAffinityEnabled') is not None:
            self.zone_affinity_enabled = m.get('ZoneAffinityEnabled')

        return self

class ListVpcEndpointServicesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the instance. You can specify up to 20 tag keys. The key cannot be an empty string.
        # 
        # The key can be up to 64 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the instance. You can specify up to 20 tag values. The value can be an empty string.
        # 
        # The value can be up to 128 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
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

