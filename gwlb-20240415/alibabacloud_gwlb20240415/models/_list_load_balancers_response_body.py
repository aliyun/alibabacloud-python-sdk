# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gwlb20240415 import models as main_models
from darabonba.model import DaraModel

class ListLoadBalancersResponseBody(DaraModel):
    def __init__(
        self,
        load_balancers: List[main_models.ListLoadBalancersResponseBodyLoadBalancers] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The GWLB instances.
        self.load_balancers = load_balancers
        # The number of entries per page. Valid values: 1 to 1000. Default value: 20.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If NextToken is empty, no next page exists.
        # *   You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.load_balancers:
            for v1 in self.load_balancers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LoadBalancers'] = []
        if self.load_balancers is not None:
            for k1 in self.load_balancers:
                result['LoadBalancers'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.load_balancers = []
        if m.get('LoadBalancers') is not None:
            for k1 in m.get('LoadBalancers'):
                temp_model = main_models.ListLoadBalancersResponseBodyLoadBalancers()
                self.load_balancers.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListLoadBalancersResponseBodyLoadBalancers(DaraModel):
    def __init__(
        self,
        address_ip_version: str = None,
        create_time: str = None,
        load_balancer_business_status: str = None,
        load_balancer_id: str = None,
        load_balancer_name: str = None,
        load_balancer_status: str = None,
        resource_group_id: str = None,
        tags: List[main_models.ListLoadBalancersResponseBodyLoadBalancersTags] = None,
        vpc_id: str = None,
        zone_mappings: List[main_models.ListLoadBalancersResponseBodyLoadBalancersZoneMappings] = None,
    ):
        # The IP version. Valid values:
        # 
        # *   **IPv4**
        self.address_ip_version = address_ip_version
        # The time when the resource was created. The time follows the ISO 8601 standard in the **yyyy-MM-ddTHH:mm:ssZ** format. The time is displayed in UTC.
        self.create_time = create_time
        # The business status of the GWLB instance. Valid values:
        # 
        # *   **Normal**: running as expected
        # *   **FinancialLocked**: locked due to overdue payments
        self.load_balancer_business_status = load_balancer_business_status
        # The GWLB instance ID.
        self.load_balancer_id = load_balancer_id
        # The GWLB instance name.
        # 
        # The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter.
        self.load_balancer_name = load_balancer_name
        # The GWLB instance status. Valid values:
        # 
        # *   **Active**: The GWLB instance is running.
        # *   **Inactive**: The GWLB instance is disabled. Listeners of GWLB instances in the Inactive state do not forward traffic.
        # *   **Provisioning**: The GWLB instance is being created.
        # *   **Configuring**: The GWLB instance is being modified.
        self.load_balancer_status = load_balancer_status
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The tags.
        self.tags = tags
        # The VPC ID.
        self.vpc_id = vpc_id
        # The mappings between zones and vSwitches. You must specify at least one zone. You can specify at most 20 zones. If the region supports two or more zones, specify at least two zones.
        self.zone_mappings = zone_mappings

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.zone_mappings:
            for v1 in self.zone_mappings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_ip_version is not None:
            result['AddressIpVersion'] = self.address_ip_version

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.load_balancer_business_status is not None:
            result['LoadBalancerBusinessStatus'] = self.load_balancer_business_status

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name

        if self.load_balancer_status is not None:
            result['LoadBalancerStatus'] = self.load_balancer_status

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        result['ZoneMappings'] = []
        if self.zone_mappings is not None:
            for k1 in self.zone_mappings:
                result['ZoneMappings'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressIpVersion') is not None:
            self.address_ip_version = m.get('AddressIpVersion')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('LoadBalancerBusinessStatus') is not None:
            self.load_balancer_business_status = m.get('LoadBalancerBusinessStatus')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')

        if m.get('LoadBalancerStatus') is not None:
            self.load_balancer_status = m.get('LoadBalancerStatus')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListLoadBalancersResponseBodyLoadBalancersTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        self.zone_mappings = []
        if m.get('ZoneMappings') is not None:
            for k1 in m.get('ZoneMappings'):
                temp_model = main_models.ListLoadBalancersResponseBodyLoadBalancersZoneMappings()
                self.zone_mappings.append(temp_model.from_map(k1))

        return self

class ListLoadBalancersResponseBodyLoadBalancersZoneMappings(DaraModel):
    def __init__(
        self,
        load_balancer_addresses: List[main_models.ListLoadBalancersResponseBodyLoadBalancersZoneMappingsLoadBalancerAddresses] = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The GWLB instance addresses.
        self.load_balancer_addresses = load_balancer_addresses
        # The ID of the vSwitch in the zone. By default, each zone contains one vSwitch and one subnet.
        self.v_switch_id = v_switch_id
        # The zone ID. You can call the DescribeZones operation to query the most recent zone list.
        self.zone_id = zone_id

    def validate(self):
        if self.load_balancer_addresses:
            for v1 in self.load_balancer_addresses:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LoadBalancerAddresses'] = []
        if self.load_balancer_addresses is not None:
            for k1 in self.load_balancer_addresses:
                result['LoadBalancerAddresses'].append(k1.to_map() if k1 else None)

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.load_balancer_addresses = []
        if m.get('LoadBalancerAddresses') is not None:
            for k1 in m.get('LoadBalancerAddresses'):
                temp_model = main_models.ListLoadBalancersResponseBodyLoadBalancersZoneMappingsLoadBalancerAddresses()
                self.load_balancer_addresses.append(temp_model.from_map(k1))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class ListLoadBalancersResponseBodyLoadBalancersZoneMappingsLoadBalancerAddresses(DaraModel):
    def __init__(
        self,
        eni_id: str = None,
        private_ipv_4address: str = None,
    ):
        # The ID of the elastic network interface (ENI) used by the GWLB instance.
        self.eni_id = eni_id
        # The private IPv4 address.
        self.private_ipv_4address = private_ipv_4address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eni_id is not None:
            result['EniId'] = self.eni_id

        if self.private_ipv_4address is not None:
            result['PrivateIpv4Address'] = self.private_ipv_4address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EniId') is not None:
            self.eni_id = m.get('EniId')

        if m.get('PrivateIpv4Address') is not None:
            self.private_ipv_4address = m.get('PrivateIpv4Address')

        return self

class ListLoadBalancersResponseBodyLoadBalancersTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 128 characters in length. The tag key cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The tag value. You can specify at most 20 tag values. The tag value cannot be an empty string.
        # 
        # The tag value can be up to 128 characters in length. It must start with a letter and can contain digits, periods (.), underscores (_), and hyphens (-). It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
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

