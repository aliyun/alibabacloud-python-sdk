# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gwlb20240415 import models as main_models
from darabonba.model import DaraModel

class ListLoadBalancersRequest(DaraModel):
    def __init__(
        self,
        address_ip_version: str = None,
        load_balancer_business_status: str = None,
        load_balancer_ids: List[str] = None,
        load_balancer_names: List[str] = None,
        load_balancer_status: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_group_id: str = None,
        skip: int = None,
        tag: List[main_models.ListLoadBalancersRequestTag] = None,
        traffic_mode: str = None,
        vpc_ids: List[str] = None,
        zone_ids: List[str] = None,
    ):
        # The IP version of the NLB instance. Valid values:
        # 
        # *   **Ipv4**
        # 
        # Enumeration values:
        # 
        # *   IPv4: IPv4
        # *   DualStack: dual-stack
        self.address_ip_version = address_ip_version
        # The business status of the GWLB instance. Valid values:
        # 
        # *   **Normal**: running as expected
        # *   **FinancialLocked**: locked due to overdue payments
        self.load_balancer_business_status = load_balancer_business_status
        # The GWLB instance IDs. You can query at most 20 GWLB instances in each call.
        self.load_balancer_ids = load_balancer_ids
        # The GWLB instance names. You can specify at most 20 GWLB instance names in each call.
        self.load_balancer_names = load_balancer_names
        # The GWLB instance status. Valid values:
        # 
        # *   **Active**: The GWLB instance is running.
        # *   **Inactive**: The GWLB instance is disabled. Listeners of GWLB instances in the Inactive state do not forward traffic.
        # *   **Provisioning**: The GWLB instance is being created.
        # *   **Configuring**: The GWLB instance is being modified.
        self.load_balancer_status = load_balancer_status
        # The number of entries per page. Valid values: 1 to 1000. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value of **NextToken** is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The number of entries to be skipped in the call.
        self.skip = skip
        # The tags. You can specify up to 20 tags in each call.
        self.tag = tag
        # Specifies the traffic processing mode. Valid values:
        # 
        # *   **LoadBalance**: load balancing mode. GWLB continues to forward traffic to backend servers.
        # *   **ByPass**: bypass mode. GWLB directly returns traffic to the GWLB endpoint without forwarding it to the backend servers.
        self.traffic_mode = traffic_mode
        # The virtual private cloud (VPC) IDs. You can query at most 20 IDs in each call.
        self.vpc_ids = vpc_ids
        # The zone IDs. You can query at most 20 zone IDs in each call.
        self.zone_ids = zone_ids

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

        if self.load_balancer_business_status is not None:
            result['LoadBalancerBusinessStatus'] = self.load_balancer_business_status

        if self.load_balancer_ids is not None:
            result['LoadBalancerIds'] = self.load_balancer_ids

        if self.load_balancer_names is not None:
            result['LoadBalancerNames'] = self.load_balancer_names

        if self.load_balancer_status is not None:
            result['LoadBalancerStatus'] = self.load_balancer_status

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.skip is not None:
            result['Skip'] = self.skip

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.traffic_mode is not None:
            result['TrafficMode'] = self.traffic_mode

        if self.vpc_ids is not None:
            result['VpcIds'] = self.vpc_ids

        if self.zone_ids is not None:
            result['ZoneIds'] = self.zone_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressIpVersion') is not None:
            self.address_ip_version = m.get('AddressIpVersion')

        if m.get('LoadBalancerBusinessStatus') is not None:
            self.load_balancer_business_status = m.get('LoadBalancerBusinessStatus')

        if m.get('LoadBalancerIds') is not None:
            self.load_balancer_ids = m.get('LoadBalancerIds')

        if m.get('LoadBalancerNames') is not None:
            self.load_balancer_names = m.get('LoadBalancerNames')

        if m.get('LoadBalancerStatus') is not None:
            self.load_balancer_status = m.get('LoadBalancerStatus')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Skip') is not None:
            self.skip = m.get('Skip')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListLoadBalancersRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TrafficMode') is not None:
            self.traffic_mode = m.get('TrafficMode')

        if m.get('VpcIds') is not None:
            self.vpc_ids = m.get('VpcIds')

        if m.get('ZoneIds') is not None:
            self.zone_ids = m.get('ZoneIds')

        return self

class ListLoadBalancersRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. You cannot specify an empty string as a tag key.
        # 
        # The tag key can be up to 128 characters in length, cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The tag value. It can be up to 256 characters in length and cannot contain `http://` or `https://`.
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

