# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListIpamDiscoveredIpAddressesRequest(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        ip_version: str = None,
        ipam_resource_discovery_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.cidr = cidr
        self.ip_version = ip_version
        # This parameter is required.
        self.ipam_resource_discovery_id = ipam_resource_discovery_id
        self.max_results = max_results
        self.next_token = next_token
        # This parameter is required.
        self.region_id = region_id
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.ipam_resource_discovery_id is not None:
            result['IpamResourceDiscoveryId'] = self.ipam_resource_discovery_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('IpamResourceDiscoveryId') is not None:
            self.ipam_resource_discovery_id = m.get('IpamResourceDiscoveryId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

