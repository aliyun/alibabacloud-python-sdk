# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_epg20260715 import models as main_models
from darabonba.model import DaraModel

class AddIpAddressesToEgressProxyIpPoolRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        egress_proxy_ip_pool_id: str = None,
        zone_mappings: List[main_models.AddIpAddressesToEgressProxyIpPoolRequestZoneMappings] = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        # This parameter is required.
        self.egress_proxy_ip_pool_id = egress_proxy_ip_pool_id
        # This parameter is required.
        self.zone_mappings = zone_mappings

    def validate(self):
        if self.zone_mappings:
            for v1 in self.zone_mappings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.egress_proxy_ip_pool_id is not None:
            result['EgressProxyIpPoolId'] = self.egress_proxy_ip_pool_id

        result['ZoneMappings'] = []
        if self.zone_mappings is not None:
            for k1 in self.zone_mappings:
                result['ZoneMappings'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EgressProxyIpPoolId') is not None:
            self.egress_proxy_ip_pool_id = m.get('EgressProxyIpPoolId')

        self.zone_mappings = []
        if m.get('ZoneMappings') is not None:
            for k1 in m.get('ZoneMappings'):
                temp_model = main_models.AddIpAddressesToEgressProxyIpPoolRequestZoneMappings()
                self.zone_mappings.append(temp_model.from_map(k1))

        return self

class AddIpAddressesToEgressProxyIpPoolRequestZoneMappings(DaraModel):
    def __init__(
        self,
        ip_addresses: List[main_models.AddIpAddressesToEgressProxyIpPoolRequestZoneMappingsIpAddresses] = None,
        ip_count: int = None,
        zone_id: str = None,
    ):
        self.ip_addresses = ip_addresses
        self.ip_count = ip_count
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        if self.ip_addresses:
            for v1 in self.ip_addresses:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IpAddresses'] = []
        if self.ip_addresses is not None:
            for k1 in self.ip_addresses:
                result['IpAddresses'].append(k1.to_map() if k1 else None)

        if self.ip_count is not None:
            result['IpCount'] = self.ip_count

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ip_addresses = []
        if m.get('IpAddresses') is not None:
            for k1 in m.get('IpAddresses'):
                temp_model = main_models.AddIpAddressesToEgressProxyIpPoolRequestZoneMappingsIpAddresses()
                self.ip_addresses.append(temp_model.from_map(k1))

        if m.get('IpCount') is not None:
            self.ip_count = m.get('IpCount')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self



class AddIpAddressesToEgressProxyIpPoolRequestZoneMappingsIpAddresses(DaraModel):
    def __init__(
        self,
        eip_allocation_id: str = None,
        private_ipv_4address: str = None,
    ):
        self.eip_allocation_id = eip_allocation_id
        self.private_ipv_4address = private_ipv_4address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eip_allocation_id is not None:
            result['EipAllocationId'] = self.eip_allocation_id

        if self.private_ipv_4address is not None:
            result['PrivateIpv4Address'] = self.private_ipv_4address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EipAllocationId') is not None:
            self.eip_allocation_id = m.get('EipAllocationId')

        if m.get('PrivateIpv4Address') is not None:
            self.private_ipv_4address = m.get('PrivateIpv4Address')

        return self

