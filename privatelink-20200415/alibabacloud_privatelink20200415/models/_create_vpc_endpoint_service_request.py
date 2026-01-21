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
        # The protocol. Valid values:
        # 
        # *   **IPv4** (default)
        # *   **DualStack**
        # 
        # >  You can set the protocol to DualStack only for endpoint services whose backend resource type is NLB. An endpoint service supports dual-stack only if its backend resources support dual-stack.
        self.address_ip_version = address_ip_version
        # Specifies whether to automatically accept endpoint connection requests. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.auto_accept_enabled = auto_accept_enabled
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request.
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The payer. Valid values:
        # 
        # *   **Endpoint**: service consumer
        # *   **EndpointService**: service provider
        self.payer = payer
        # The region ID of the endpoint service.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/120468.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The service resources of the endpoint service. You can create at most 10 resources. After the resource is created, you can continue to add service resources to the endpoint.
        self.resource = resource
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The description of the endpoint service.
        self.service_description = service_description
        # The type of the service resource. Valid values:
        # 
        # *   **slb**: Classic Load Balancer (CLB) instance
        # *   **alb**: Application Load Balancer (ALB) instance
        # *   **nlb**: Network Load Balancer (NLB) instance
        # 
        # >  You cannot access TCP/SSL listeners configured for NLB instances.
        self.service_resource_type = service_resource_type
        # Specifies whether to enable IPv6 for the endpoint service. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.service_support_ipv_6 = service_support_ipv_6
        self.supported_region_list = supported_region_list
        # The tags to add to the resource.
        self.tag = tag
        # Specifies whether to first resolve the domain name of the nearest endpoint that is associated with the endpoint service. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
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
        # The key of the tag to add to the resource. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `aliyun` or `acs:`.
        self.key = key
        # The value of the tag to add to the resource. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag value cannot start with `aliyun` or `acs:`.
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
        # The type of the service resource that is added to the endpoint service. You can add up to 20 service resources to the endpoint service. Valid values:
        # 
        # *   **slb**: CLB instance
        # *   **alb**: ALB instance
        # *   **nlb**: NLB instance
        # 
        # >  In regions where PrivateLink is supported, CLB instances deployed in virtual private clouds (VPCs) can serve as the service resources of the endpoint service. You cannot access TCP/SSL listeners configured for NLB instances.
        self.resource_type = resource_type
        # The zone ID of the cluster.
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

