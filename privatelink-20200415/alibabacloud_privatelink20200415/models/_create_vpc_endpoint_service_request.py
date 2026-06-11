# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_privatelink20200415 import models as main_models
from darabonba.model import DaraModel

class CreateVpcEndpointServiceRequest(DaraModel):
    def __init__(
        self,
        address_ip_version: str = None,
        auto_accept_enabled: bool = None,
        client_token: str = None,
        dry_run: bool = None,
        payer: str = None,
        region_id: str = None,
        resource: List[main_models.CreateVpcEndpointServiceRequestResource] = None,
        resource_group_id: str = None,
        service_description: str = None,
        service_resource_type: str = None,
        service_support_ipv_6: bool = None,
        supported_region_list: List[str] = None,
        tag: List[main_models.CreateVpcEndpointServiceRequestTag] = None,
        zone_affinity_enabled: bool = None,
    ):
        # The IP version. Valid values:
        # 
        # - **IPv4** (default): IPv4.
        # - **DualStack**: dual stack.
        # > Only endpoint services whose backend resource type is nlb or gwlb support DualStack. If the endpoint service supports dual stack, its backend resources must also support dual stack.
        self.address_ip_version = address_ip_version
        # Specifies whether to automatically accept endpoint connection requests. Valid values:
        # 
        # - **true**: automatically accepts endpoint connection requests.
        # 
        # - **false** (default): does not automatically accept endpoint connection requests.
        self.auto_accept_enabled = auto_accept_enabled
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among different requests. **ClientToken** can contain only ASCII characters.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # - **true**: performs only a dry run. The system checks the request for required parameters, request format, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # 
        # - **false** (default): performs a dry run and sends the request. If the request passes the dry run, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The payer of the endpoint service. Valid values:
        # 
        # - **Endpoint**: the service consumer.
        # 
        # - **EndpointService**: the service provider.
        self.payer = payer
        # The ID of the region where the endpoint service is created.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/469325.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The list of service resources of the endpoint service. You can add at most 10 service resources when you create the endpoint service. After the endpoint service is created, you can continue to add service resources.
        self.resource = resource
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The description of the endpoint service.
        self.service_description = service_description
        # The type of the service resource. Valid values:
        # 
        # - **slb**: a Classic Load Balancer (CLB) instance.
        # 
        # - **alb**: an Application Load Balancer (ALB) instance.
        # - **nlb**: a Network Load Balancer (NLB) instance.
        # - **gwlb**: a Gateway Load Balancer (GWLB) instance.
        # 
        # > TCPSSL listeners of NLB instances cannot be accessed.
        self.service_resource_type = service_resource_type
        # Specifies whether the endpoint service supports IPv6. Valid values:
        # 
        # - **true**: yes.
        # 
        # - **false** (default): no.
        self.service_support_ipv_6 = service_support_ipv_6
        # The list of regions in which the endpoint service is available. Service consumers can initiate endpoint connections from the regions in the list.
        self.supported_region_list = supported_region_list
        # The tag list.
        self.tag = tag
        # Specifies whether to enable zone affinity for endpoint domain name resolution. Valid values:
        # 
        # - **true**: yes.
        # 
        # - **false** (default): no.
        self.zone_affinity_enabled = zone_affinity_enabled

    def validate(self):
        if self.resource:
            for v1 in self.resource:
                 if v1:
                    v1.validate()
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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.payer is not None:
            result['Payer'] = self.payer

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['Resource'] = []
        if self.resource is not None:
            for k1 in self.resource:
                result['Resource'].append(k1.to_map() if k1 else None)

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.service_description is not None:
            result['ServiceDescription'] = self.service_description

        if self.service_resource_type is not None:
            result['ServiceResourceType'] = self.service_resource_type

        if self.service_support_ipv_6 is not None:
            result['ServiceSupportIPv6'] = self.service_support_ipv_6

        if self.supported_region_list is not None:
            result['SupportedRegionList'] = self.supported_region_list

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

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Payer') is not None:
            self.payer = m.get('Payer')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.resource = []
        if m.get('Resource') is not None:
            for k1 in m.get('Resource'):
                temp_model = main_models.CreateVpcEndpointServiceRequestResource()
                self.resource.append(temp_model.from_map(k1))

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ServiceDescription') is not None:
            self.service_description = m.get('ServiceDescription')

        if m.get('ServiceResourceType') is not None:
            self.service_resource_type = m.get('ServiceResourceType')

        if m.get('ServiceSupportIPv6') is not None:
            self.service_support_ipv_6 = m.get('ServiceSupportIPv6')

        if m.get('SupportedRegionList') is not None:
            self.supported_region_list = m.get('SupportedRegionList')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateVpcEndpointServiceRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('ZoneAffinityEnabled') is not None:
            self.zone_affinity_enabled = m.get('ZoneAffinityEnabled')

        return self

class CreateVpcEndpointServiceRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. You can specify at most 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be at most 64 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The tag value. You can specify at most 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be at most 128 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
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

class CreateVpcEndpointServiceRequestResource(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        zone_id: str = None,
    ):
        # The ID of the service resource that is added to the endpoint service.
        self.resource_id = resource_id
        # The type of the service resource that is added to the endpoint service. You can add at most 20 service resources to an endpoint service. Valid values:
        # 
        # - **slb**: a Classic Load Balancer (CLB) instance.
        # 
        # - **alb**: an Application Load Balancer (ALB) instance.
        # - **nlb**: a Network Load Balancer (NLB) instance.
        # - **gwlb**: a Gateway Load Balancer (GWLB) instance.
        self.resource_type = resource_type
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

