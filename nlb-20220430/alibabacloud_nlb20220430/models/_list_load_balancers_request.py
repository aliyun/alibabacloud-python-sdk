# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nlb20220430 import models as main_models
from darabonba.model import DaraModel

class ListLoadBalancersRequest(DaraModel):
    def __init__(
        self,
        address_ip_version: str = None,
        address_type: str = None,
        dnsname: str = None,
        ipv_6address_type: str = None,
        load_balancer_business_status: str = None,
        load_balancer_ids: List[str] = None,
        load_balancer_names: List[str] = None,
        load_balancer_status: str = None,
        load_balancer_type: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tag: List[main_models.ListLoadBalancersRequestTag] = None,
        vpc_ids: List[str] = None,
        zone_id: str = None,
    ):
        # The IP version of the NLB instance. Valid values:
        # 
        # *   **ipv4**: IPv4
        # *   **DualStack**: dual-stack
        self.address_ip_version = address_ip_version
        # The type of IPv4 address used by the NLB instance. Valid values:
        # 
        # *   **Internet**: The NLB instance uses a public IP address. The domain name of the NLB instance is resolved to the public IP address. The NLB instance can be accessed over the Internet.
        # *   **Intranet**: The NLB instance uses a private IP address. The domain name of the NLB instance is resolved to the private IP address. The NLB instance can be accessed over the VPC where the NLB instance is deployed.
        self.address_type = address_type
        # The domain name of the NLB instance.
        self.dnsname = dnsname
        # The type of IPv6 address used by the NLB instance. Valid values:
        # 
        # *   **Internet**: The NLB instance uses a public IP address. The domain name of the NLB instance is resolved to the public IP address. The NLB instance can be accessed over the Internet.
        # *   **Intranet**: The NLB instance uses a private IP address. The domain name of the NLB instance is resolved to the private IP address. The NLB instance can be accessed over the VPC where the NLB instance is deployed.
        self.ipv_6address_type = ipv_6address_type
        # The business status of the NLB instance. Valid values:
        # 
        # *   **Abnormal**: The NLB instance is not working as expected.
        # *   **Normal**: The NLB instance is working as expected.
        self.load_balancer_business_status = load_balancer_business_status
        # The NLB instance IDs. You can specify up to 20 IDs in each call.
        self.load_balancer_ids = load_balancer_ids
        # The names of the NLB instances. You can specify up to 20 names in each call.
        self.load_balancer_names = load_balancer_names
        # The status of the NLB instance. Valid values:
        # 
        # *   **Inactive**: The NLB instance is disabled. Listeners of an NLB instance in the Inactive state do not forward traffic.
        # *   **Active**: The NLB instance is running.
        # *   **Provisioning**: The NLB instance is being created.
        # *   **Configuring**: The NLB instance is being modified.
        # *   **Deleting**: The NLB instance is being deleted.
        # *   **Deleted**: The NLB instance is deleted.
        self.load_balancer_status = load_balancer_status
        # The type of the Server Load Balancer (SLB) instances. Set the value to **network**, which specifies NLB.
        self.load_balancer_type = load_balancer_type
        # The number of entries to return in each call. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results
        # The pagination token used to specify a particular page of results. Valid values:
        # 
        # *   Leave this parameter empty for the first query or the only query.
        # *   Set this parameter to the value of NextToken obtained from the previous query.
        self.next_token = next_token
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/443657.html) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The tags of the NLB instance.
        self.tag = tag
        # The IDs of the virtual private clouds (VPCs) where the NLB instances are deployed. You can specify up to 10 VPC IDs in each call.
        self.vpc_ids = vpc_ids
        # The ID of the zone. You can call the [DescribeZones](https://help.aliyun.com/document_detail/443890.html) operation to query the most recent zone list.
        self.zone_id = zone_id

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

        if self.address_type is not None:
            result['AddressType'] = self.address_type

        if self.dnsname is not None:
            result['DNSName'] = self.dnsname

        if self.ipv_6address_type is not None:
            result['Ipv6AddressType'] = self.ipv_6address_type

        if self.load_balancer_business_status is not None:
            result['LoadBalancerBusinessStatus'] = self.load_balancer_business_status

        if self.load_balancer_ids is not None:
            result['LoadBalancerIds'] = self.load_balancer_ids

        if self.load_balancer_names is not None:
            result['LoadBalancerNames'] = self.load_balancer_names

        if self.load_balancer_status is not None:
            result['LoadBalancerStatus'] = self.load_balancer_status

        if self.load_balancer_type is not None:
            result['LoadBalancerType'] = self.load_balancer_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.vpc_ids is not None:
            result['VpcIds'] = self.vpc_ids

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressIpVersion') is not None:
            self.address_ip_version = m.get('AddressIpVersion')

        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        if m.get('DNSName') is not None:
            self.dnsname = m.get('DNSName')

        if m.get('Ipv6AddressType') is not None:
            self.ipv_6address_type = m.get('Ipv6AddressType')

        if m.get('LoadBalancerBusinessStatus') is not None:
            self.load_balancer_business_status = m.get('LoadBalancerBusinessStatus')

        if m.get('LoadBalancerIds') is not None:
            self.load_balancer_ids = m.get('LoadBalancerIds')

        if m.get('LoadBalancerNames') is not None:
            self.load_balancer_names = m.get('LoadBalancerNames')

        if m.get('LoadBalancerStatus') is not None:
            self.load_balancer_status = m.get('LoadBalancerStatus')

        if m.get('LoadBalancerType') is not None:
            self.load_balancer_type = m.get('LoadBalancerType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListLoadBalancersRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VpcIds') is not None:
            self.vpc_ids = m.get('VpcIds')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class ListLoadBalancersRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag. You can specify up to 20 tags. The tag key cannot be an empty string.
        # 
        # It must be 1 to 64 characters in length, cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The value of the tag. You can specify up to 20 tags. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length, cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
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

