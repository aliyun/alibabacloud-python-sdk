# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpcipam20230228 import models as main_models
from darabonba.model import DaraModel

class ListIpamDiscoveredIpAddressesResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        ipam_discovered_ip_addresses: List[main_models.ListIpamDiscoveredIpAddressesResponseBodyIpamDiscoveredIpAddresses] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.count = count
        self.ipam_discovered_ip_addresses = ipam_discovered_ip_addresses
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.ipam_discovered_ip_addresses:
            for v1 in self.ipam_discovered_ip_addresses:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['IpamDiscoveredIpAddresses'] = []
        if self.ipam_discovered_ip_addresses is not None:
            for k1 in self.ipam_discovered_ip_addresses:
                result['IpamDiscoveredIpAddresses'].append(k1.to_map() if k1 else None)

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
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.ipam_discovered_ip_addresses = []
        if m.get('IpamDiscoveredIpAddresses') is not None:
            for k1 in m.get('IpamDiscoveredIpAddresses'):
                temp_model = main_models.ListIpamDiscoveredIpAddressesResponseBodyIpamDiscoveredIpAddresses()
                self.ipam_discovered_ip_addresses.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListIpamDiscoveredIpAddressesResponseBodyIpamDiscoveredIpAddresses(DaraModel):
    def __init__(
        self,
        ip_address: str = None,
        ip_version: str = None,
        resource_id: str = None,
        resource_region_id: str = None,
        resource_service_type: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.ip_address = ip_address
        self.ip_version = ip_version
        self.resource_id = resource_id
        self.resource_region_id = resource_region_id
        self.resource_service_type = resource_service_type
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id

        if self.resource_service_type is not None:
            result['ResourceServiceType'] = self.resource_service_type

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')

        if m.get('ResourceServiceType') is not None:
            self.resource_service_type = m.get('ResourceServiceType')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

