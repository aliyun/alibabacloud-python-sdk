# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_privatelink20200415 import models as main_models
from darabonba.model import DaraModel

class CreateVpcEndpointRequest(DaraModel):
    def __init__(
        self,
        address_ip_version: str = None,
        client_token: str = None,
        cross_region_bandwidth: int = None,
        dry_run: bool = None,
        endpoint_description: str = None,
        endpoint_name: str = None,
        endpoint_type: str = None,
        policy_document: str = None,
        protected_enabled: bool = None,
        region_id: str = None,
        resource_group_id: str = None,
        security_group_id: List[str] = None,
        service_id: str = None,
        service_name: str = None,
        service_region_id: str = None,
        tag: List[main_models.CreateVpcEndpointRequestTag] = None,
        vpc_id: str = None,
        zone: List[main_models.CreateVpcEndpointRequestZone] = None,
        zone_affinity_enabled: bool = None,
        zone_private_ip_address_count: int = None,
    ):
        # The protocol. Valid values:
        # 
        # *   **IPv4** (default)
        # *   **DualStack**
        # 
        # >  An endpoint supports dual-stack if its associated endpoint service and VPC both support dual-stack.
        self.address_ip_version = address_ip_version
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        self.client_token = client_token
        self.cross_region_bandwidth = cross_region_bandwidth
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The description of the endpoint.
        # 
        # The description must be 2 to 256 characters in length, and cannot start with `http://` or `https://`.
        self.endpoint_description = endpoint_description
        # The name of the endpoint.
        # 
        # The name must be 2 to 128 characters in length, and can contain digits, underscores (_), and hyphens (-). The name must start with a letter.
        self.endpoint_name = endpoint_name
        # The endpoint type. Valid values:
        # 
        # *   **Interface** You can specify an Application Load Balancer (ALB) instance, a Classic Load Balancer (CLB) instance, or a Network Load Balancer (NLB) instance.
        # *   **Reverse** You can specify a Virtual Private Cloud (VPC) NAT gateway.
        # 
        # >  Services that support reverse endpoints are provided by Alibaba Cloud or Alibaba Cloud partners. To create such a service on your own, contact your account manager.
        self.endpoint_type = endpoint_type
        self.policy_document = policy_document
        # Specifies whether to enable user authentication. This parameter is available in Security Token Service (STS) mode. Valid values:
        # 
        # *   **true**: enables user authentication. After user authentication is enabled, only the user who creates the endpoint can modify or delete the endpoint in STS mode.
        # *   **false** (default): disables user authentication.
        self.protected_enabled = protected_enabled
        # The region ID of the endpoint.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/120468.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The IDs of security groups that are associated with the endpoint elastic network interface (ENI).
        self.security_group_id = security_group_id
        # The ID of the endpoint service with which the endpoint is associated.
        self.service_id = service_id
        # The name of the endpoint service with which the endpoint is associated.
        self.service_name = service_name
        self.service_region_id = service_region_id
        # The tags to add to the resource.
        self.tag = tag
        # The ID of the virtual private cloud (VPC) to which the endpoint belongs.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The zones where the endpoint is deployed.
        self.zone = zone
        self.zone_affinity_enabled = zone_affinity_enabled
        # The number of private IP addresses that are assigned to an elastic network interface (ENI) in each zone. Set the value to **1**.
        self.zone_private_ip_address_count = zone_private_ip_address_count

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()
        if self.zone:
            for v1 in self.zone:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_ip_version is not None:
            result['AddressIpVersion'] = self.address_ip_version

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cross_region_bandwidth is not None:
            result['CrossRegionBandwidth'] = self.cross_region_bandwidth

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.endpoint_description is not None:
            result['EndpointDescription'] = self.endpoint_description

        if self.endpoint_name is not None:
            result['EndpointName'] = self.endpoint_name

        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type

        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document

        if self.protected_enabled is not None:
            result['ProtectedEnabled'] = self.protected_enabled

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        result['Zone'] = []
        if self.zone is not None:
            for k1 in self.zone:
                result['Zone'].append(k1.to_map() if k1 else None)

        if self.zone_affinity_enabled is not None:
            result['ZoneAffinityEnabled'] = self.zone_affinity_enabled

        if self.zone_private_ip_address_count is not None:
            result['ZonePrivateIpAddressCount'] = self.zone_private_ip_address_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressIpVersion') is not None:
            self.address_ip_version = m.get('AddressIpVersion')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CrossRegionBandwidth') is not None:
            self.cross_region_bandwidth = m.get('CrossRegionBandwidth')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EndpointDescription') is not None:
            self.endpoint_description = m.get('EndpointDescription')

        if m.get('EndpointName') is not None:
            self.endpoint_name = m.get('EndpointName')

        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')

        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')

        if m.get('ProtectedEnabled') is not None:
            self.protected_enabled = m.get('ProtectedEnabled')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateVpcEndpointRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        self.zone = []
        if m.get('Zone') is not None:
            for k1 in m.get('Zone'):
                temp_model = main_models.CreateVpcEndpointRequestZone()
                self.zone.append(temp_model.from_map(k1))

        if m.get('ZoneAffinityEnabled') is not None:
            self.zone_affinity_enabled = m.get('ZoneAffinityEnabled')

        if m.get('ZonePrivateIpAddressCount') is not None:
            self.zone_private_ip_address_count = m.get('ZonePrivateIpAddressCount')

        return self

class CreateVpcEndpointRequestZone(DaraModel):
    def __init__(
        self,
        ipv_6address: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
        ip: str = None,
    ):
        # The IPv6 address of the zone where the endpoint is deployed.
        # 
        # >  You can specify this parameter only if AddressIpVersion is set to DualStack.
        self.ipv_6address = ipv_6address
        # The ID of the vSwitch for which you want to create the endpoint elastic network interface (ENI) in the zone. You can specify up to 10 vSwitches.
        self.v_switch_id = v_switch_id
        # The ID of the zone where the endpoint service is deployed.
        # 
        # You can specify up to 10 zones.
        self.zone_id = zone_id
        # The IP address of the zone where the endpoint is deployed.
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_6address is not None:
            result['Ipv6Address'] = self.ipv_6address

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        if self.ip is not None:
            result['ip'] = self.ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv6Address') is not None:
            self.ipv_6address = m.get('Ipv6Address')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('ip') is not None:
            self.ip = m.get('ip')

        return self



class CreateVpcEndpointRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag to add to the resource.
        self.key = key
        # The value of the tag to add to the resource.
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

