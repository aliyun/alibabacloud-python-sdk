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
        # The protocol version. Valid values:
        # - **ipv4**: IPv4.
        # - **DualStack**: dual-stack.
        self.address_ip_version = address_ip_version
        # The IPv4 address type of the NLB instance. Valid values:
        # - **Internet**: The load balancing instance has a public IP address. The DNS domain name is resolved to the public IP address. Therefore, the instance is accessible over the Internet.
        # - **Intranet**: The load balancing instance has only a private IP address. The DNS domain name is resolved to the private IP address. Therefore, the instance is accessible only within the internal network environment of the VPC where the load balancing instance is deployed.
        self.address_type = address_type
        # The DNS domain name.
        self.dnsname = dnsname
        # The IPv6 address type of the NLB instance. Valid values:
        # - **Internet**: The load balancing instance has a public IP address. The DNS domain name is resolved to the public IP address. Therefore, the instance is accessible over the Internet.
        # - **Intranet**: The load balancing instance has only a private IP address. The DNS domain name is resolved to the private IP address. Therefore, the instance is accessible only within the internal network environment of the VPC where the load balancing instance is deployed.
        self.ipv_6address_type = ipv_6address_type
        # The business status of the NLB instance. Valid values:
        # - **Abnormal**: The instance is in an abnormal state.
        # - **Normal**: The instance is in a normal state.
        self.load_balancer_business_status = load_balancer_business_status
        # The IDs of the NLB instances. You can query up to 20 instances at a time.
        self.load_balancer_ids = load_balancer_ids
        # The names of the NLB instances. You can query up to 20 instance names at a time.
        self.load_balancer_names = load_balancer_names
        # The status of the NLB instance. Valid values:
        # - **Inactive**: The instance is stopped. Listeners of the instance no longer forward traffic.
        # - **Active**: The instance is running.
        # - **Provisioning**: The instance is being created.
        # - **Configuring**: Upgrade/Downgrade in progress.
        # - **Deleting**: The instance is being deleted.
        # - **Deleted**: The instance is deleted.
        self.load_balancer_status = load_balancer_status
        # The type of load balancing. Only **network** is returned, which indicates Network Load Balancer (NLB).
        self.load_balancer_type = load_balancer_type
        # The number of entries per page. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # - If this is the first request or no next request exists, you do not need to specify this parameter.
        # - If a next request exists, set the value to the NextToken value returned in the previous API call.
        self.next_token = next_token
        # The region ID of the NLB instance. 
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/443657.html) operation to query the most recent region list.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The labels of the NLB instance.
        self.tag = tag
        # The VPC ID of the NLB instance. You can query up to 10 VPC IDs at a time.
        self.vpc_ids = vpc_ids
        # The zone name. You can call the [DescribeZones](https://help.aliyun.com/document_detail/443890.html) operation to query zones.
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
        # The tag key of the instance. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the instance. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
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

